from django.contrib import admin
from app.models import *

# Register your models here.
class userregister(admin.ModelAdmin):
    list_display=['name','email']

admin.site.register(UserRegister,userregister)

admin.site.register(Question)