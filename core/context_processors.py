from courses.models import Course
def academy_data(request):
    return {"courses": Course.objects.filter(is_active=True)[:6]}
