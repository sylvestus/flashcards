from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('newflash/<int:id>',views.new_flash_card,name='newflash'),
    path('flashcards/<int:id>',views.flashcards_in_subject,name='flashcards'),
    path('profile/',views.profile,name='profile'),
    path('showProfile',views.profile,name='showProfile'),
    path('showProfile/update/<int:id>',views.uprofile,name='uprofile'),
    path('newsubject/',views.new_subject,name='newsubject'), 
   
    
]
