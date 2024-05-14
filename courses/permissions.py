from rest_framework.permissions import BasePermission

from courses.models import CourseStudent


class IsAdminOrEnrolledToCourse(BasePermission):
    message = 'Доступ к урокам курса не разрешен. Запишитесь на курс, чтобы иметь возможность просматривать уроки'
    
    def has_permission(self, request, view):
        user = request.user
        if user.is_superuser:
            return True
        
        course_slug = view.kwargs.get('course_slug')
        student = CourseStudent.objects.filter(user__username=user.username).filter(course__slug=course_slug)
        
        return True if student else False
