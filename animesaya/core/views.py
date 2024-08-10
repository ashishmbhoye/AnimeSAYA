from django.shortcuts import render
from wallpapers.models import desktop_images,mobile_images
from . forms import form_register
from django.shortcuts import redirect
import random
# Create your views here.
def home(request):
    desktop=list(desktop_images.objects.all())
    mobile=list(mobile_images.objects.all())
    images=desktop+mobile
    img_list=list(images)
    data=random.sample(desktop,8)
    random.shuffle(img_list)
    return render(request,'core/home.html',{'img':data,'images':img_list})

def register(request):
    form=form_register(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/login/')
    context={
        'form':form
    }
    
    return render(request,'core/register.html',context)
