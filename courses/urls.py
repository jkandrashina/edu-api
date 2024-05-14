from django.urls import path

from courses.views import (
    CoursesView,
    CourseLessonsView,
)


urlpatterns = [
    path('courses/', CoursesView.as_view()),
	path('courses/<str:course_slug>/', CourseLessonsView.as_view()),
]