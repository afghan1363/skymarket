from rest_framework.permissions import BasePermission


# TODO здесь производится настройка пермишенов для нашего проекта

# **Пользователь может:**
#
# - получать список объявлений,
# - получать одно объявление,
# - создавать объявление
# - редактировать и удалять свое объявление,
# - получать список комментариев,
# - создавать комментарии,
# - редактировать/удалять свои комментарии.
#
# **Администратор может:**
#
# дополнительно к правам пользователя редактировать или удалять
# объявления и комментарии любых других пользователей.


class IsAuthorOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.user.is_admin or request.user.is_superuser
