from django.urls import path, include
from rest_framework.routers import SimpleRouter

from ads.apps import SalesConfig
# from ads.views import (AdCreateAPIView, AdRetrieveAPIView, AdListAPIView, CommentCreateAPIView, CommentRetrieveAPIView,
#                        AdMeListAPIView, AdUpdateAPIView, AdDestroyAPIView, CommentListAPIView, CommentUpdateAPIView,
#                        CommentDestroyAPIView)
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

# urlpatterns = [
#     path('api/ads/', views.AdCreateAPIView.as_view(), name='create_ad'),
#     path('api/ads/<int:pk>/', views.AdRetrieveAPIView.as_view(), name='detail_ad'),
#     path('api/ads/', views.AdListAPIView.as_view(), name='list_ad'),
#     path('api/ads/me/', views.AdMeListAPIView.as_view(), name='list_ad_me'),
#     path('api/ads/<int:pk>/', views.AdUpdateAPIView.as_view(), name='update_ad'),
#     path('api/ads/<int:pk>/', views.AdDestroyAPIView.as_view(), name='delete_ad'),
#
#     path('api/ads/<int:pk>/comments/', views.CommentCreateAPIView.as_view(), name='create_comment'),
#     path('api/ads/<int:ad_pk>/comments/<int:pk>/', views.CommentRetrieveAPIView.as_view(), name='detail_comment'),
#     path('api/ads/<int:ad_pk>/comments/', views.CommentListAPIView.as_view(), name='list_comment'),
#     path('api/ads/<int:ad_pk>/comments/<int:pk>/', views.CommentUpdateAPIView.as_view(), name='update_comment'),
#     path('api/ads/<int:ad_pk>/comments/<int:pk>/', views.CommentDestroyAPIView.as_view(), name='delete_comment'),
# ]
