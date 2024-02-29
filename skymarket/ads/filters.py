import django_filters
from ads.models import Ad


class TitleSearchFilter(django_filters.rest_framework.FilterSet):
    """
    Класс поиска объявлений по заголовку
    """
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains", )

    class Meta:
        model = Ad
        fields = ("title",)
