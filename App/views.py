from django.shortcuts import render,redirect
from .models import Mails
from django.core.mail import send_mail 
# Create your views here.

def Portfolio(request):
    return render(request,'Portfolio.html')

def add(request):
    mails = Mails.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        maildate = request.POST.get('maildate')

        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        mail = Mails(
            maildate=maildate,
            name=name,
            email=email,
            mobile=mobile,
            subject=subject,
            message=message,
        )
        mail.save()


        send_mail(subject,' Name :- '+ name +' Phone Number :- ' + mobile + ' Email ID :- ' + email + ' Date :-' + maildate + '.                                                                                           Message :- ' + message
                ,email,[email,'atulguptacontact@gmail.com'],fail_silently=False)        

        return redirect('Portfolio')

    return render(request,'Portfolio.html' , context = {"mails":mails})