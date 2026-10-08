from django.contrib import admin
from .models import Course, Lesson, Assignment
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "duration", "price", "is_active")
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Lesson)
admin.site.register(Assignment)
