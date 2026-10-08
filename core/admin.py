from django.contrib import admin
from .models import Instructor, Testimonial, StudentProject, ContactMessage
admin.site.register(Instructor)
admin.site.register(Testimonial)
admin.site.register(StudentProject)
admin.site.register(ContactMessage)
