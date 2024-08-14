from django.shortcuts import render
from . models import desktop_images,mobile_images
from . forms import form_desktop,form_mobile
from django.shortcuts import redirect,get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
import random
from django.db.models import Q
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


@login_required
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



def image_search_bar(request):
    image_query = request.GET.get("image_query", "")
    print(image_query)  # Debug print to show the query received

    search_result = []
    
    if image_query:
        # Get results from both desktop and mobile images using the query
        desktop_search_results = desktop_images.objects.filter(name__icontains=image_query)
        mobile_search_results = mobile_images.objects.filter(name__icontains=image_query)

        # Combine the results into a single list
        search_result = list(desktop_search_results) + list(mobile_search_results)
        print("IMAGE SEARCH RESULT :", search_result)

        # Ensure each image has an 'id' and 'type' field
        for img in search_result:
            img.id = getattr(img, 'id', None)
            img.type = getattr(img, 'type', None)
    
    # Prepare the context with the combined results
    context = {
        "images_from_DB": search_result,
        "image_query":image_query
    }
    
    return render(request, "wallpapers/wallpapers.html", context)


def mobile_search_bar(request):
    mobile_image_query = request.GET.get("image_query", "")
    print(mobile_image_query)  # Debug print to show the query received
    
    if mobile_image_query == "":
        # mobile_imgs= mobile_images.objects.all()
        return redirect("mobile_images")
        # return render(request, "wallpapers/wallpapers.html", {"mobile_data":mobile_imgs})
    else:

        search_result = []
        
        if mobile_image_query:
            # Get results from both desktop and mobile images using the query
        
            mobile_search_results = mobile_images.objects.filter(name__icontains=mobile_image_query)

            # Combine the results into a single list
            # mobile_search_result = mobile_search_results
            print("IMAGE SEARCH RESULT :", mobile_search_results)

            # Ensure each image has an 'id' and 'type' field
            for img in mobile_search_results:
                img.id = getattr(img, 'id', None)
                img.type = getattr(img, 'type', None)
        
        # Prepare the context with the combined results
        context = {
            "mobile_images_from_DB": mobile_search_results,
            "mobile_image_query":mobile_image_query
        }
        
        return render(request, "wallpapers/mobile_wallpapers.html", context)