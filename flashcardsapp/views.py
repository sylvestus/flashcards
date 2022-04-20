from django.shortcuts import render

# Create your views here.
def home(request):
    message='welcome home'
    return render(request,'home.html',{'message':message})

def new_flash_card(request):
    message='post new flashcards here'
    return render(request,'newflash.html',{'message':message})
