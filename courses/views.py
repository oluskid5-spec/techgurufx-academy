from django.shortcuts import get_object_or_404, render
from .models import Course

def course_list(request):
    category = request.GET.get("category")
    courses = Course.objects.filter(is_active=True)
    if category in {"tech", "forex"}: courses = courses.filter(category=category)
    return render(request, "courses/courses.html", {"courses": courses, "selected": category})

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug, is_active=True)
    return render(request, "courses/course_detail.html", {"course": course})
