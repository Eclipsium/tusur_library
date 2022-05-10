from django.contrib import admin

# Register your models here.
from library.models import University, Faculty, Student, Author, Book, IssuedBook


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ("abbr", 'name', 'foundation')
    list_display_links = ('name', "abbr", 'foundation')
    search_fields = ["abbr", "name"]


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ("abbr", 'name', 'university')
    list_display_links = ('name', "abbr", 'university')
    search_fields = ["abbr", "name"]
    autocomplete_fields = ["university"]
    list_filter = ('university',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('last_name', "first_name", 'faculty')
    list_display_links = ('last_name', "first_name", 'faculty')
    search_fields = ['last_name', "first_name"]
    list_filter = ('faculty',)
    autocomplete_fields = ["faculty"]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', "first_name")
    list_display_links = ('last_name', "first_name")
    search_fields = ['last_name', "first_name"]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    filter_horizontal = ('author',)
    list_display = ('title', "authors", 'published', "isbn")
    list_display_links = ('title', "authors", 'published', "isbn")
    search_fields = ('title',)
    list_filter = ('author',)

    def authors(self, obj):
        return ", ".join([str(p) for p in obj.author.all()])


@admin.register(IssuedBook)
class IssuedBookAdmin(admin.ModelAdmin):
    list_display = ('student', "book", 'date_of_issue', "return_date", "is_return")
    list_display_links = (
        'student', "book", 'date_of_issue', "return_date", "is_return"
    )
    search_fields = ("book__title", "student__first_name", "student__last_name")
    list_filter = ("date_of_issue", "return_date", 'is_return')
    autocomplete_fields = ["student", "book"]


"J&*^JmUAvwrze89m"