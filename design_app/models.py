from django.db import models

# Create your models here.
class ImageGallary(models.Model):
    image_name =models.CharField(max_length=100)
    image =models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.image_name
    
class VedioGallary(models.Model):
    vedio_name=models.CharField(max_length=100)
    vedio=models.FileField(upload_to='vedio')

    def __str__(self):
        return self.vedio_name
    
class Contact(models.Model):
    name=models.CharField(max_length=60)
    mobile =models.CharField(max_length=12)
    email=models.EmailField(max_length=20)
    msz=models.CharField(max_length=500)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.name
    

class FeedBack(models.Model):
    name=models.CharField(max_length=60)
    mobile =models.CharField(max_length=12)
    email=models.EmailField(max_length=20)
    feedback=models.CharField(max_length=500)
    interior=models.IntegerField(null=True)
    exterior =models.IntegerField(null=True)
    overall=models.IntegerField(null=True)
    suggest=models.CharField(max_length=5)
    def __str__(self):
        return self.name
