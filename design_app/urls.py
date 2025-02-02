
from django.urls import path 
from design_app import views
urlpatterns = [
    path('', views.design,name='design'),
    path('contact', views.contact,name='contact'),
    path('designGallary', views.designGallary,name='designGallary'),
    path('vedioGallary', views.vedioGallary,name='vedioGallary'),
    path('about', views.about,name='about'),
    path('feedback', views.feedback,name='feedback'),
   
]
