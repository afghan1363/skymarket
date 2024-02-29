from rest_framework.permissions import BasePermission


class IsAuthorOrAdmin(BasePermission):
    """
    Класс прав доступа для автора записей либо для администратора
    """
    message = 'Только автор может удалить или изменить'

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.user.is_admin or request.user.is_superuser
