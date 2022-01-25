from django.contrib import admin
from .models import Profile  #we register our models here so that we can view them from admin page
# Register your models here.


admin.site.register(Profile)
