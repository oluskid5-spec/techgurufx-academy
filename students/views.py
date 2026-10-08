from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render
from .forms import StudentRegistrationForm

def register(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            messages.success(request, "Welcome to TechGuruFx Academy!")
            return redirect("dashboard")
    else: form = StudentRegistrationForm()
    return render(request, "accounts/register.html", {"form": form})
