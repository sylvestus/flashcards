from django.shortcuts import render

# Create your views here.
def home(request):
    message='welcome home'
    return render(request,'home.html',{'message':message})
