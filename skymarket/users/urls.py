from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'users'

users_router = SimpleRouter()

users_router.register(prefix='users', viewset=UserViewSet, basename='users')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + users_router.urls

# GET "users/" — список профилей пользователей
# POST "users/" — регистрация пользователя
# GET, PATCH, DELETE "users/{id}" — в соответствии с REST и необходимыми permissions (для администратора)
# GET PATCH "users/me" — получение и изменение своего профиля
# POST "users/set_password" — ручка для изменения пароля
# POST "users/reset_password" — ручка для направления ссылки сброса пароля на email*
# POST "users/reset_password_confirm" — ручка для сброса своего пароля*
