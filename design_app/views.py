from django.shortcuts import render,redirect
from .models import ImageGallary
from .models import VedioGallary
from .models import Contact
from .models import FeedBack
from django.contrib import messages

def design(request):
      con ={"intro":"WelCome To Maa Janaki Construction",
          }
      
      return render(request,'design.html',con)

def contact(request):
    con ={"intro":"Contact Us",
          }
    if request.method=='POST':
          name= request.POST['name']
          mobile=request.POST['phone']
          email=request.POST['email']
          msz=request.POST['msz']
          if len(name)<2 or len(email)<3 or len(mobile)<10 or len(msz)<4:
            messages.error(request, "Please fill the form correctly")
          else:
            contact=Contact(name=name,mobile=mobile,email=email,msz=msz) 
            contact.save() 
            messages.success(request, "Your message has been successfully sent")
    return render(request,'contact.html',con)

def about(request):
    con ={"intro":"About Us",
          }
    return render(request,'about.html',con)

def designGallary(request):
    all_design=ImageGallary.objects.all
    con ={"intro":"PHOTO GALLERY",
          "all_design":all_design}
    return render(request,'designgallary.html',con)

def vedioGallary(request):
    all_vedio=VedioGallary.objects.all
    con ={"intro":"VEDIO GALLERY",
          "all_vedio":all_vedio}
    return render(request,'vediogallary.html',con)


def feedback(request):
    con ={"intro":"Your Feed Back is important For Us!",
          }
    if request.method=='POST':
          name= request.POST['name']
          mobile=request.POST['phone']
          email=request.POST['email']
          msz=request.POST['msz']
          interior=request.POST['Interior']
          exterior=request.POST['Exterior']
          overall=request.POST['OverAll']
          suggest=request.POST['Suggest']
          if len(name)<2 or len(email)<3 or len(mobile)<10 or len(msz)<4:
            messages.error(request, "Please fill the form correctly")
          else:
            feedback=FeedBack(name=name,mobile=mobile,email=email,feedback=msz,interior=interior,exterior=exterior,overall=overall,suggest=suggest) 
            feedback.save() 
            messages.success(request, "Your Feedback has been successfully Submitted")
    return render(request,'feedback.html',con)