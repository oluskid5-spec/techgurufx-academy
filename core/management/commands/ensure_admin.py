
import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create or reset a designated administrator."

    def handle(self, *args, **options):
        database_url = os.environ.get("DATABASE_URL", "")
        username = os.environ.get("ADMIN_USERNAME")
        password = os.environ.get("ADMIN_PASSWORD")
        email = os.environ.get("ADMIN_EMAIL", "")

        if not username or not password:
            self.stdout.write(
                "Admin recovery variables not set; skipping."
            )
            return

        if not database_url.startswith(
            ("postgres://", "postgresql://")
        ):
            raise CommandError(
                "Refusing admin recovery: DATABASE_URL "
                "must point to PostgreSQL."
            )

        if len(password) < 12:
            raise CommandError(
                "ADMIN_PASSWORD must be at least 12 characters."
            )

        User = get_user_model()

        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            created = False
        else:
            user = User(username=username)
            created = True

        user.email = email
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

        action = "created" if created else "updated"
        self.stdout.write(
            self.style.SUCCESS(
                f"Administrator {action} successfully."
            )
        )
