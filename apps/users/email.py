import random

from django.core.mail import send_mail

from .models import CustomUser


def send_email_confirm(email):
    subject = 'Подтверждение регистрации'
    message = f"""Здравствуйте! Ваш адрес электронной почты был указан для входа на приложение Yummy. 
    Пожалуйста, введите этот код на странице авторизации:<<< {random.randint(100000, 999999)} >>> 
    Если это не вы или вы не регистрировались на сайте, то просто проигнорируйте это письмо"""
    email_from = 'admin@gmail.com'
    send_mail(subject, message, email_from, [email])
    user_obj = CustomUser.objects.get(email=email)
    user_obj.code = random.randint(100000, 999999)
    user_obj.save()


def send_email_reset_password(email, recovery_code):
    subject = "Восстановление пароля"
    message = f"Код для восстановления пароля: <<< {recovery_code} >>> Код действителен в течении 5 минут"
    email_from = 'admin@gmail.com'
    send_mail(subject, message, email_from, [email])
