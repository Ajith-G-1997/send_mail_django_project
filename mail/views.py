from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render



def home(request):
    return render(request,'base.html')

# views.py
def send_email(request):
    send_mail(
        'Hello from Ajith',
        'This is a test email Sending By Ajith G.',
        'sender@example.com',
        ['recipient@example.com'],
        fail_silently=False,
    )
    return render(request, 'send_email.html')


