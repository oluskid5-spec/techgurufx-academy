from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Enrollment, LessonProgress

@login_required
def dashboard(request):
    enrollments = Enrollment.objects.filter(student=request.user).select_related("course")
    return render(request, "portal/dashboard.html", {
        "enrollments": enrollments,
        "progress": LessonProgress.objects.filter(student=request.user, completed=True).count(),
    })
