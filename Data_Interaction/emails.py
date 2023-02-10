from django.core.mail import send_mail
import random
from django.conf import settings 
from .models import User


# def check_mail(email):
# 	subject = 'Please use the OTP code below to reset your account password !'
# 	otp = random.randint(100000,999999)
# 	message = f'Your OTP is {otp}'
# 	email_from = settings.EMAIL_HOST
# 	send_mail(subject, message, email_from, [email])
# 	user_obj = User.objects.get(email=email)
# 	user_obj.otp = otp
# 	user_obj.save()

def send_otp(email):
	subject = 'Please use the OTP code below to reset your account password !'
	otp = random.randint(100000,999999)
	message = f'Your OTP is {otp}'
	email_from = settings.EMAIL_HOST
	send_mail(subject, message, email_from, [email])
	user_obj = User.objects.get(email=email)
	user_obj.otp = otp
	user_obj.save()

