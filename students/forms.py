from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import StudentProfile

class StudentRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField()
    phone = forms.CharField(max_length=30, required=False)
    class Meta:
        model = User
        fields = ("username","first_name","last_name","email","phone","password1","password2")
    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit: StudentProfile.objects.create(user=user, phone=self.cleaned_data.get("phone",""))
        return user
