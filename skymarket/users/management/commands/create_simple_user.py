from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        email = input('email: ')
        first_name = input('first_name: ')
        last_name = input('last_name: ')
        phone = input('phone: ')
        password = input('password: ')
        user = User.objects.create(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            role='user'
        )
        user.set_password(password)
        user.save()
