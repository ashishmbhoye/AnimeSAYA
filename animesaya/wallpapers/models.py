from django.db import models

# Create your models here.
class desktop_images(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True)
    img=models.ImageField(upload_to='wallpapers', height_field=None, width_field=None, max_length=None)
    type=models.CharField( max_length=50,default='desktop')

    class Meta:
        db_table = 'desktop'

    def __str__(self) -> str:
        return self.name
    
class mobile_images(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True)
    img=models.ImageField(upload_to='wallpapers', height_field=None, width_field=None, max_length=None)
    type=models.CharField(max_length=50,default='mobile')

    class Meta:
        db_table = 'mobile'

    def __str__(self) -> str:
        return self.name
    
    
    