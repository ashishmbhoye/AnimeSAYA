from django import forms
from . models import desktop_images,mobile_images


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result

class form_desktop(forms.ModelForm):
    img = MultipleFileField()

    class Meta:
        model = desktop_images
        fields = ['img']
 

class form_mobile(forms.ModelForm):
    img = MultipleFileField()
    
    class Meta:
        model=mobile_images
        fields=['img']

