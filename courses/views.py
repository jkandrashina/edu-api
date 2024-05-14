from datetime import date, datetime

from django.db.models import Count

from rest_framework.generics import (
    ListAPIView
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)
from rest_framework.response import Response

from courses.models import (
    Course,
    CourseStudent,
)
from courses.serializers import (
    CourseSerializer,
    CourseLessonsSerializer,
)
from courses.permissions import IsAdminOrEnrolledToCourse


class CoursesView(ListAPIView):
    queryset = Course.objects.filter(date_start__gte = date.today()).prefetch_related('lessons').annotate(lessons_count=Count('lessons'))
    
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CourseLessonsView(ListAPIView):
    def get_queryset(self):
        course_slug = self.kwargs.get('course_slug')
        lessons_list = Course.objects.filter(slug=course_slug).prefetch_related('lessons')
        return lessons_list
    
    serializer_class = CourseLessonsSerializer
    permission_classes = [IsAuthenticated, IsAdminOrEnrolledToCourse]
