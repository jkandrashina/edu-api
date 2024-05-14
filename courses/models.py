from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    date_start = models.DateField(
        verbose_name='Дата старта'
    )
    time_start = models.TimeField(
        verbose_name='Время старта'
    )
    price = models.PositiveIntegerField(
        verbose_name='Стоимость'
    )
    min_students_in_group = models.PositiveIntegerField(
        default=1,
        verbose_name='Минимальное количество студентов в группе'
    )
    max_students_in_group = models.PositiveIntegerField(
        default=10,
        verbose_name='Максимальное количество студентов в группе'
    )
    slug = models.SlugField(
        verbose_name='URL'
    )
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'author', 'date_start'], name='unique_course_date_start')
        ]
        verbose_name = ('Курс')
        verbose_name_plural = ('Курсы')
    
    def __str__(self):
        return f'{self.title} ({self.author})'


class Lesson(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='lessons',
        verbose_name='Курс'
    )
    title = models.CharField(
        max_length=200,
        verbose_name='Название'
    )
    video_url = models.URLField(
        max_length=200,
        verbose_name='Ссылка на видео'
    )
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['video_url'], name='unique_video_link')
        ]
        verbose_name = ('Урок')
        verbose_name_plural = ('Уроки')
    
    def __str__(self):
        return self.title


class CourseStudent(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Студент'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='Курс'
    )
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'course'], name='unique_course_student')
        ]
        verbose_name = ('Студент курса')
        verbose_name_plural = ('Студенты курса')
    
    def __str__(self):
        return self.user.username


class CourseGroup(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='course_groups',
        verbose_name='Курс'
    )
    group_name = models.CharField(
        max_length=100,
        verbose_name='Название группы'
    )
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['group_name'], name='unique_group_name')
        ]
        verbose_name = ('Группа курса')
        verbose_name_plural = ('Группы курса')
    
    def __str__(self):
        return self.group_name


class StudentsInGroup(models.Model):
    group = models.ForeignKey(
        CourseGroup,
        on_delete=models.CASCADE,
        related_name='students',
        verbose_name='Группа курса'
    )
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Студент'
    )
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['group', 'student'], name='unique_group_student')
        ]
        verbose_name = ('Студент в группе')
        verbose_name_plural = ('Студенты в группе')
    
    def __str__(self):
        return f'{self.student} {self.group}'    

