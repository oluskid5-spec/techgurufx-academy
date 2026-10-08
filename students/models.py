from django.conf import settings
from django.db import models

class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to="students/", blank=True, null=True)
    def __str__(self): return self.user.get_full_name() or self.user.username
