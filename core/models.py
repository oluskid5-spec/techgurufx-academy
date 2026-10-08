from django.db import models

class Instructor(models.Model):
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    bio = models.TextField()
    photo = models.ImageField(upload_to="instructors/", blank=True, null=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    def __str__(self): return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=150, blank=True)
    message = models.TextField()
    is_published = models.BooleanField(default=True)
    def __str__(self): return self.name

class StudentProject(models.Model):
    student_name = models.CharField(max_length=150)
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=250)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    project_url = models.URLField(blank=True)
    def __str__(self): return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.name} - {self.subject}"
