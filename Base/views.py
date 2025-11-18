from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from Base import models
from Base.models import Contact
# Create your views here.

# def home(request):
#     return render(request,'home.html')
def contact(request):
    if request.method=="POST":
        print('post')
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('number')
        content=request.POST.get('content')
        print(name,email,phone,content)


        if len(name)>1 and len(name)<30:
            pass
        else:
            messages.error(request,'Length of name is invalid')
            return render(request,'home.html')
        if len(email)>1 and len(email)<30:
            pass
        else:
            messages.error(request,'invalid email try again')
            return render(request,'home.html')
        
        if len(phone)>9 and len(phone)<11:
            pass
        else:
            messages.error(request,'invalid phone number try again')
            return render(request,'home.html')
        ins=models.Contact(name=name,email=email,phone=phone,content=content)
        ins.save()
        messages.success(request,'Thank you for contacting us.We will get back to you soon')
        print('data saved to database')
        print('the request is no pass')
    return render(request,'home.html')


