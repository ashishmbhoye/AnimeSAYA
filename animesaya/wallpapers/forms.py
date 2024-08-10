from django import forms
from . models import desktop_images,mobile_images

class form_desktop(forms.ModelForm):
    class Meta:
        model=desktop_images
        fields=['name','img']
 

class form_mobile(forms.ModelForm):
     class Meta:
        model=mobile_images
        fields=['name','img']
 
