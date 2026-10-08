from django.db import models
from django.urls import reverse

class Course(models.Model):
    CATEGORY_CHOICES = [("tech", "Technology"), ("forex", "Forex")]
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    duration = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(upload_to="courses/", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    def get_absolute_url(self): return reverse("course_detail", kwargs={"slug": self.slug})
    def __str__(self): return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.PositiveIntegerField(default=1)
    class Meta: ordering = ["order"]
    def __str__(self): return self.title

class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="assignments")
    title = models.CharField(max_length=200)
    instructions = models.TextField()
    due_date = models.DateField(blank=True, null=True)
    def __str__(self): return self.title
