from django.contrib.auth.models import User


def register_user(username, email, password):
    return User.objects.create_user(
        username=username,
        email=email,
        password=password,
    )