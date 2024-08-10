from django.shortcuts import render
from . models import desktop_images,mobile_images
from . forms import form_desktop,form_mobile
from django.shortcuts import redirect,get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
import random

# Create your views here.
def wallpapers_list(request):
    data=desktop_images.objects.all()
    image_list=list(data)
    random.shuffle(image_list)
    return render(request,'wallpapers/desk_wallpapers.html',{'img':image_list})

def mobile_wallpapers(request):
    data=mobile_images.objects.all()
    image_list=list(data)
    random.shuffle(image_list)
    return render(request,'wallpapers/mobile_wallpapers.html',{'img':image_list})

@login_required
def add_desktop_images(request):
    form=form_desktop(request.POST, request.FILES)
    context={
        'form':form,
        'msg':'Image Added Successfully'
    }
    print('thsi is desktop',form)
    if form.is_valid():
        form.save()
        return render(request,'wallpapers/desktop_add.html',context)
    context={
        'form':form
    }
    return render(request,'wallpapers/desktop_add.html',context)

@login_required
def add_mobile_images(request):
    form=form_mobile(request.POST, request.FILES)
    context={
        'form':form,
        'msg':'Image Added Successfully'
    }
    if form.is_valid():
        form.save()
        return render(request,'wallpapers/mob_add.html',context)
        
    context={
        'form':form
    }
    return render(request,'wallpapers/mob_add.html',context)

def wallpapers(request):
    desktop=desktop_images.objects.all()
    print(desktop)
    desktop=list(desktop_images.objects.all())
    print(desktop)
    mobile=list(mobile_images.objects.all())
    images=desktop+mobile
    img_list=list(images)
    random.shuffle(img_list)
    return render(request,'wallpapers/wallpapers.html',{'img':img_list})
    
def illustrate(request, id, type):
    if type == 'desktop':
        desktop = get_object_or_404(desktop_images, id=id, type="desktop")
        random_desk=list(desktop_images.objects.all())
        random_desktop=random.sample(random_desk,6)
        context = {
        'desktop': desktop,
        'random_desk':random_desktop
    }
    else:
        mobile = get_object_or_404(mobile_images, id=id, type="mobile")
        random_mob=list(mobile_images.objects.all())
        random_mobile=random.sample(random_mob,6)
        context = {
        'mobile': mobile,
        'random_mob':random_mobile
    }
   
    return render(request, 'wallpapers/ilustrate.html', context)


def download_image(request, id, type):
    if type == 'desktop':
        image = get_object_or_404(desktop_images, id=id)
    elif type == 'mobile':
        image = get_object_or_404(mobile_images, id=id)
    else:
        raise Http404("Image type not found")

    response = HttpResponse(image.img, content_type='image/jpeg') 
    response['Content-Disposition'] = f'attachment; filename="{image.name}.jpg"'
    return response
