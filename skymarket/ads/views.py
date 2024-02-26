from rest_framework import pagination, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from ads.models import Ad, Comment
from rest_framework.generics import ListAPIView
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer
from ads.permissions import IsAuthorOrAdmin
from ads.filters import TitleSearchFilter


class AdPagination(pagination.PageNumberPagination):
    """
    Класс пагинации
    """
    page_size = 4
    page_query_param = 'page_size'
    max_page_size = 50


class AdViewSet(viewsets.ModelViewSet):
    """
    Контроллер для управления моделью Объявления
    """
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = TitleSearchFilter
    ordering = ('-created_at',)

    def perform_create(self, serializer):
        """
        Метод определения автора объявления
        """
        new_ad = serializer.save()
        new_ad.author = self.request.user
        print(new_ad.author)
        new_ad.save()

    def get_serializer_class(self):
        """
        Метод установки класса сериализатора
        """
        if self.action == 'retrieve':
            return AdDetailSerializer
        else:
            return AdSerializer

    def get_permissions(self):
        """
        Метод определения прав доступа
        """
        print(self.action)
        if self.action == 'retrieve':
            permission_classes = (IsAuthenticated,)
        elif self.action == 'create':
            permission_classes = (IsAuthenticated,)
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsAuthorOrAdmin]
        else:
            permission_classes = (AllowAny,)
        return [permission() for permission in permission_classes]


class AdMeListAPIView(ListAPIView):
    """
    Контроллер вывода списка объявлений текущего авторизированного пользователя
    """
    serializer_class = AdSerializer
    filter_backends = (OrderingFilter,)
    filterset_class = TitleSearchFilter
    ordering = ('-created_at',)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        Метод запроса данных текущего авторизированного пользователя
        """
        return Ad.objects.filter(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Контроллер для управления моделью Отзывы
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        """
        Метод определения автора отзыва и определение объявления, к которому оставлен отзыв
        """
        ad_id = self.kwargs['ad_pk']
        ad = Ad.objects.get(pk=ad_id)
        new_comment = serializer.save()
        new_comment.author = self.request.user
        new_comment.ad = ad
        new_comment.save()

    def list(self, request, *args, **kwargs):
        """
        Метод для вывода списка отзывов для текущего объявления
        """
        ad_pk = self.kwargs.get('ad_pk')
        queryset = self.queryset.filter(ad_id=ad_pk)
        serializer = self.get_serializer(queryset, many=True)
        return self.get_paginated_response(self.paginate_queryset(serializer.data))

    def get_permissions(self):
        """
        Метод определения прав доступа
        """
        if self.action == 'retrieve':
            permission_classes = (IsAuthenticated,)
        elif self.action == 'create':
            permission_classes = (IsAuthenticated,)
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsAuthorOrAdmin]
        else:
            permission_classes = (AllowAny,)
        return [permission() for permission in permission_classes]
