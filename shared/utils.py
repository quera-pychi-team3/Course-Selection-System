from random import random

from django.core.mail import EmailMessage
from django.conf import settings
from django.core.cache import cache


def create_email(subject, body, to):
    return EmailMessage(from_email=settings.EMAIL_SENDER, subject=subject, body=body, to=[to, ])


def send_password_reset_email(link, to):
    body = 'Hi, \nUse link below to reset your password \n' + link
    subject = 'Reset Your Password'
    create_email(subject, body, to).send()


def generate_otp():
    otp = ''.join(random.choices('0123456789', k=6))

    cache_key = f'otp:{otp}'
    cache.set(cache_key, True, timeout=300)

    return otp


def check_otp(otp):
    cache_key = f'otp:{otp}'
    stored_value = cache.get(cache_key)

    if stored_value is not None:
        cache.delete(cache_key)
        return True
    else:
        return False