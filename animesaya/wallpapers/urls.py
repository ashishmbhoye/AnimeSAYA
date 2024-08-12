from django.urls import path
from .views import (
    wallpapers_list,
    mobile_wallpapers,
    add_desktop_images,
    add_mobile_images,
    wallpapers,
    illustrate,
    download_image,
    image_search_bar,
)

urlpatterns = [
    path('wallpapers/', wallpapers_list, name='wallpapers_list'),
    path('mobile_images/', mobile_wallpapers, name='mobile_images'),
    path('add_desktop_images/', add_desktop_images, name='add_desktop_images'),
    path('add_mobile_images/', add_mobile_images, name='add_mobile_images'),
    path('allwallpapers/', wallpapers, name='allwallpapers'),
    path('illustrate/<int:id>/<str:type>/', illustrate, name='illustrate'),
    path('download/<int:id>/<str:type>/', download_image, name='download_image'),
    path('image-search-bar/', image_search_bar, name='image_search_bar'),
]
