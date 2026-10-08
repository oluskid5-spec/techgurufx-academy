from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import ContactForm
from .models import Instructor, StudentProject, Testimonial

def home(request):
    return render(request, "core/home.html", {
        "instructors": Instructor.objects.all()[:3],
        "testimonials": Testimonial.objects.filter(is_published=True)[:3],
        "projects": StudentProject.objects.all()[:6],
    })

def about(request):
    return render(request, "core/about.html", {"instructors": Instructor.objects.all()})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks! Your message has been sent.")
            return redirect("contact")
    else:
        form = ContactForm()
    return render(request, "core/contact.html", {"form": form})
