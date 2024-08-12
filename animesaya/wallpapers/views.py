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

# @login_required
def add_desktop_images(request):
    if request.method == 'POST':
        form = form_desktop(request.POST, request.FILES)
        if form.is_valid():
            # name = form.cleaned_data['name']
            images = request.FILES.getlist('img')
            print("Images from form:",images)
            for image in images:
                print("IMAGE from for loop:",image)
                print("IMAGE type from for loop:",type(str(image)))
                image_name=str(image)
                print("Image name :",image_name)
                image_name_after_split=image_name.split(".")[0]
                print("Image name after split :",image_name_after_split)
                desktop_images.objects.create(name=image_name_after_split, img=image)
            return redirect('wallpapers_list')
    else:
        form = form_desktop()
    return render(request, 'wallpapers/desktop_add.html', {"form": form})


# @login_required
def add_mobile_images(request):
        if request.method == 'POST':
            form = form_mobile(request.POST, request.FILES)
            if form.is_valid():
                # name = form.cleaned_data['name']
                images = request.FILES.getlist('img')
                print("Images from form:",images)
                for image in images:
                    print("IMAGE from for loop:",image)
                    print("IMAGE type from for loop:",type(str(image)))
                    image_name=str(image)
                    print("Image name :",image_name)
                    image_name_after_split=image_name.split(".")[0]
                    print("Image name after split :",image_name_after_split)
                    mobile_images.objects.create(name=image_name_after_split, img=image)
                return redirect('mobile_images')
        else:
            form = form_mobile()
        return render(request, 'wallpapers/mob_add.html', {"form": form})

def wallpapers(request):
    # desktop=desktop_images.objects.all()
    # print(desktop)
    desktop=list(desktop_images.objects.all())
    # print(desktop)
    mobile=list(mobile_images.objects.all())
    print(mobile)
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
