from django.contrib import admin
from courses.models import (
    Course,
    Lesson,
    CourseStudent,
    CourseGroup,
    StudentsInGroup,
)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_start', 'price', 'id')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')


@admin.register(CourseStudent)
class CourseStudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course')


@admin.register(CourseGroup)
class CourseGroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'course')


@admin.register(StudentsInGroup)
class StudentsInGroupAdmin(admin.ModelAdmin):
    list_display = ('student', 'group')
