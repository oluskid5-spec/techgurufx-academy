# TechGuruFx Academy

A Django academy website inspired by the layout patterns of the free ThemeWagon Purdue educational template: hero header, sticky navigation, course cards, statistics, testimonials, instructors, CTA and detailed footer.

The implementation is original and uses Bootstrap 5.3 via CDN. It is connected to Django models so courses, instructors, testimonials and student projects can be managed from Django Admin.

## Run locally

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/courses/
- http://127.0.0.1:8000/students/register/
- http://127.0.0.1:8000/portal/
- http://127.0.0.1:8000/admin/

## Theme note

The public ThemeWagon Purdue page describes the free template as Bootstrap 5.3.3 with a hero header, sticky navigation, course cards, testimonial sections, fun-fact counters, CTA, responsive design and multipage support. This project recreates those structural ideas for TechGuruFx Academy with original HTML/CSS/content rather than copying proprietary source files.

Replace placeholder academy contact information in `templates/core/contact.html` and the footer when your real details are ready.
