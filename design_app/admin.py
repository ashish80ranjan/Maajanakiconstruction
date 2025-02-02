from django.contrib import admin

# Register your models here.
from .models import Contact
from .models import VedioGallary
from .models import ImageGallary
from .models import FeedBack

admin.site.register(Contact)
admin.site.register(VedioGallary)
admin.site.register(ImageGallary)
admin.site.register(FeedBack)