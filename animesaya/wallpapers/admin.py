from django.contrib import admin
from . models import desktop_images,mobile_images


@admin.register(desktop_images)
class admindesktop(admin.ModelAdmin):
    list_display=['id','name','img','type']

@admin.register(mobile_images)
class adminmobie(admin.ModelAdmin):
    list_display=['id','name','img','type']


