from django.urls import path, include
from rest_framework.routers import SimpleRouter
from ads.apps import SalesConfig
from ads import views

app_name = SalesConfig.name

ads_router = SimpleRouter()
ads_router.register(prefix=r'ads', viewset=views.AdViewSet, basename='ads')
comments_router = SimpleRouter()
comments_router.register(prefix=r'comments', viewset=views.CommentViewSet, basename='comments')

urlpatterns = [
    path('api/ads/me/', views.AdMeListAPIView.as_view(), name='list_ad_me'),
    path('api/', include(ads_router.urls)),
    path('api/ads/<int:ad_pk>/', include(comments_router.urls), name='comments'),
]
