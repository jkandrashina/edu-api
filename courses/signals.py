from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver

from courses.models import (
    CourseStudent,
    CourseGroup,
    StudentsInGroup
)


@receiver(post_save, sender=CourseStudent)
def add_student_to_group(sender, instance, created, **kwargs):
    if created:
        student = instance.user
        course = instance.course
        available_groups = CourseGroup.objects.filter(course=course).prefetch_related('students').annotate(students_count=Count('students')).order_by('-id')

        if (available_groups 
        and available_groups[0].students_count < instance.course.max_students_in_group):
            StudentsInGroup.objects.create(group=available_groups[0], student=student)
            return
        group_name = course.title + str(available_groups.count() + 1)
        new_group = CourseGroup.objects.create(course=course, group_name=group_name)
        new_student_in_group = StudentsInGroup.objects.create(group=new_group, student=student)

