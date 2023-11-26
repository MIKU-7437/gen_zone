from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    """
    Пользователь может редактировать только свои объекты.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        if hasattr(obj, 'course'):
            return obj.course.owner == request.user

        if hasattr(obj, 'owner'):
            return obj.owner == request.user

        if hasattr(obj, 'module') and hasattr(obj.module, 'course'):
            return obj.module.course.owner == request.user
        
        if hasattr(obj, 'lesson') and hasattr(obj.lesson, 'module'):
            return obj.lesson.module.course.owner == request.user

        return False
    