from django.shortcuts import render,redirect
from .models import ImageGallary
from .models import VedioGallary
from .models import Contact
from .models import FeedBack
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


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
            form_data = {
            'name':name,
            'email':email,
            'phone':mobile,
            'message':msz,
            }
            message = '''
            From:\t\t{}\n
            Message:\t\t{}\n
            Email:\t\t{}\n
            Phone:\t\t{}\n
            '''.format(form_data['name'], form_data['message'], form_data['email'],form_data['phone'])
            send_mail(f'You got a Contact mail From -{name}', message, '', [settings.EMAIL_HOST_USER])
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
    con ={"intro":"FeedBack Form",
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
            form_data = {
            'name':name,
            'email':email,
            'phone':mobile,
            'message':msz,
            'intrat':interior,
            'extrat':exterior,
            'overat':overall,
            'suggest':suggest
            }
            message = '''
            From:\t\t{}\n
            Message:\t\t{}\n
            Email:\t\t{}\n
            Phone:\t\t{}\n
            Interior_Rating:\t\t{}\n
            Exterior_Rating:\t\t{}\n
            Overall_Rating:\t\t{}\n
            Suugest_to_other:\t\t{}\n
            '''.format(form_data['name'], form_data['message'], form_data['email'],form_data['phone'],form_data['intrat'],form_data['extrat'],form_data['overat'],form_data['suggest'])
            send_mail(f'FeedBack from -{name}', message, '', [settings.EMAIL_HOST_USER])
            messages.success(request, "Your Feedback has been successfully Submitted")
    return render(request,'feedback.html',con)