from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('newflash/',views.new_flash_card,name='newflash'),
]