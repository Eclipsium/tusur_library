from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class University(models.Model):
    name = models.CharField("название университета", max_length=100, null=False)
    abbr = models.CharField("арбревиатура университета", max_length=10, null=False)
    foundation = models.DateField("дата основания университета")

    def __str__(self):
        return f'{self.abbr}'

    class Meta:
        verbose_name = "университет"
        verbose_name_plural = "университеты"


class Faculty(models.Model):
    name = models.CharField("название факультета", max_length=100, null=False)
    abbr = models.CharField("арбревиатура факультета", max_length=10, null=False)
    university = models.ForeignKey(University, verbose_name="университет", null=True,
                                   on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.abbr}: {self.university}'

    class Meta:
        verbose_name = "факультет"
        verbose_name_plural = "факультеты"


class Author(models.Model):
    last_name = models.CharField("фамилия", max_length=20, null=False)
    first_name = models.CharField("имя", max_length=20, null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "автор"
        verbose_name_plural = "авторы"


class Student(models.Model):
    last_name = models.CharField("фамилия", max_length=20, null=False)
    first_name = models.CharField("имя", max_length=20, null=False)
    faculty = models.ForeignKey(Faculty, verbose_name="факультет", null=True,
                                on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.faculty}"

    class Meta:
        verbose_name = "студент"
        verbose_name_plural = "студенты"


class Book(models.Model):
    title = models.CharField("название книги", max_length=100, null=False)
    author = models.ManyToManyField(Author, verbose_name="автор")
    published = models.DateField("дата выпуска")
    isbn = models.CharField("ISBN", max_length=15, null=False)

    def __str__(self):
        return f"{self.title} - " \
               f"{' '.join([author.first_name for author in self.author.all()])} - " \
               f"{self.published.year}"

    class Meta:
        verbose_name = "книга"
        verbose_name_plural = "книги"


class IssuedBook(models.Model):
    book = models.ForeignKey(Book, verbose_name="книга", on_delete=models.CASCADE)
    student = models.ForeignKey(Student, verbose_name="студент",
                                on_delete=models.CASCADE)

    date_of_issue = models.DateField(verbose_name="дата выдачи", auto_now_add=True)
    return_date = models.DateField(verbose_name="дата возврата",
                                   default=datetime.now() + timedelta(days=90))
    is_return = models.BooleanField(verbose_name="возвращено")

    def __str__(self):
        return f"{self.student} - {self.book}"

    class Meta:
        verbose_name = "выданная книга"
        verbose_name_plural = "выданные книги"
