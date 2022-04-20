from email import message
from django.shortcuts import render
from .models import Notes,Profile,Subject,Additionals

# Create your views here.
def home(request):
    message='welcome home'
    subjects=Subject.objects.all()

    return render(request,'home.html',{'message':message,'subjects':subjects})

def flashcards_in_subject(request,id):
    message='flashcards'
    flashcards=Notes.objects.filter(subject=id)
    return render(request,'flashcards.html',{'message':message,'flashcards':flashcards})

def new_flash_card(request):
    message='post new flashcards here'
    return render(request,'newflash.html',{'message':message})
