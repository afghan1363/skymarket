from rest_framework import pagination, viewsets
from rest_framework.response import Response

from ads.models import Ad, Comment
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView, DestroyAPIView
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer
from ads.permissions import IsAuthorOrAdmin


class AdPagination(pagination.PageNumberPagination):
    pass


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()

    # pagination_class =
    # filter_backends =
    # filterset_class =

    def perform_create(self, serializer):
        new_ad = serializer.save()
        new_ad.author = self.request.user
        print(new_ad.author)
        new_ad.save()

    def get_serializer_class(self):
        if self.action in ['retrieve']:
            return AdDetailSerializer
        else:
            return AdSerializer

    # def get_permissions(self):
    #     if self.action == 'retrieve':
    #         permission_classes = (IsAuthenticated)
    #     elif self.action == 'create':
    #         permission_classes = (IsAuthenticated)
    #     elif self.action in ['update', 'partial_update', 'destroy']:
    #         permission_classes = [IsAuthenticated, IsOwner | IsAdmin]
    #     else:
    #         permission_classes = [AllowAny]
    #     return [permission() for permission in permission_classes]


class AdMeListAPIView(ListAPIView):
    serializer_class = AdSerializer

    def get_queryset(self):
        return Ad.objects.filter(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        ad_id = self.kwargs['ad_pk']
        ad = Ad.objects.get(pk=ad_id)
        new_comment = serializer.save()
        new_comment.author = self.request.user
        new_comment.ad = ad
        new_comment.save()

    # def get_permissions(self):
    #     pass

    def list(self, request, *args, **kwargs):
        ad_pk = self.kwargs.get('ad_pk')
        queryset = self.queryset.filter(ad_id=ad_pk)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)




# class AdCreateAPIView(CreateAPIView):
#     serializer_class = AdSerializer
#
#     def perform_create(self, serializer):
#         new_ad = serializer.save()
#         new_ad.author = self.request.user
#         new_ad.save()
#
#
# class AdRetrieveAPIView(RetrieveAPIView):
#     queryset = Ad.objects.all()
#     serializer_class = AdDetailSerializer
#
#
# class AdUpdateAPIView(UpdateAPIView):
#     queryset = Ad.objects.all()
#     serializer_class = AdSerializer
#
#
# class AdListAPIView(ListAPIView):
#     queryset = Ad.objects.all()
#     serializer_class = AdSerializer
#
#
# class AdMeListAPIView(ListAPIView):
#     serializer_class = AdSerializer
#
#     def get_queryset(self):
#         return Ad.objects.filter(author=self.request.user)
#
#
# class AdDestroyAPIView(DestroyAPIView):
#     queryset = Ad.objects.all()
#     # ^zrobleno
#
#
# class CommentCreateAPIView(CreateAPIView):
#     serializer_class = CommentCreateSerializer
#
#     def perform_create(self, serializer):
#         ad_id = self.kwargs['ad_pk']
#         ad = Ad.objects.get(pk=ad_id)
#         new_comment = serializer.save()
#         new_comment.author = self.request.user
#         new_comment.ad = ad
#         new_comment.save()
#
#
# class CommentRetrieveAPIView(RetrieveAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentRetrieveSerializer
#
#
# class CommentUpdateAPIView(UpdateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentUpdateSerializer
#
#
# class CommentListAPIView(ListAPIView):
#     serializer_class = CommentRetrieveSerializer
#
#     def get_queryset(self):
#         ad = self.kwargs.get('id_pk')
#         return Ad.objects.filter(pk=ad).comments
#
#
# class CommentDestroyAPIView(DestroyAPIView):
#     queryset = Comment.objects.all()
