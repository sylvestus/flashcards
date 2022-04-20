from email import message
from .forms import *
from django.shortcuts import render
from .models import Notes,Profile,Subject,Additionals
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http.response import  HttpResponseRedirect
from django.shortcuts import redirect, render


# Create your views here.
def home(request):
    message='welcome home'
    subjects=Subject.objects.all()

    return render(request,'home.html',{'message':message,'subjects':subjects})


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    message='profile'
    # projects = Profile.objects.filter(user=current_user.id).all"projects": projects
    return render(request, 'profile.html', {'message':message })

@login_required(login_url='/accounts/login/')
def uprofile(request, id):
    current_user = request.user
    user_object = get_object_or_404(User, id=id)
    profile_object = get_object_or_404(Profile, user_id=id)
    profile_update = UprofileForm(request.POST or None ,request.FILES, instance=profile_object)
    user_update = UuserForm(request.POST or None, instance=user_object,)
    if profile_update.is_valid() and user_update.is_valid():
        user_update.save()
        profile_update.save()
        return HttpResponseRedirect("/showProfile")

    return render(
        request, "uprofile.html",{"profile_update": profile_update, "user_update": user_update})

def flashcards_in_subject(request,id):
    message='flashcards'
    flashcards=Notes.objects.filter(subject=id)
    return render(request,'flashcards.html',{'message':message,'flashcards':flashcards})

def new_flash_card(request,id):
    if request.method=="POST":
        current_user=request.user.profile
        note=Notes.objects.filter(id=id)
        form= Newnotes(request.POST,request.FILES)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.profile = current_user
            subject.subject= note
            subject.save()
            
        return redirect('home')
           

    else:
       
        form =  Newnotes()
    return render(request,'newflash.html',{'newflash':form,})

def deleteflascards(request,id):
    deleteflascards=Notes.objects.filter(id=id)
    deleteflascards.delete()

    return redirect('home')




@login_required(login_url='/accounts/login/')
def new_subject(request):
    if request.method=="POST":
        current_user=request.user.profile
        
        form=NewsubjectForm(request.POST,request.FILES)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.profile = current_user
            subject.save()
            
        return redirect('home')
           

    else:
       
        form = NewsubjectForm()
    return render(request,'newsubject.html',{'newsubject':form,})

@login_required(login_url='/accounts/login/')
def deletesubject(request,id):
    post=Subject.objects.filter(id=id)
    post.delete()

    return redirect('home')


# def additionals(request,id):
#     if request.method=="POST":
#         current_user=request.user.profile
#         note=Notes.objects.filter(id=id)
        
#         form= Newnotes(request.POST,request.FILES)
#         if form.is_valid():
#             subject = form.save(commit=False)
#             subject.profile = current_user
#             subject.subject= note
#             subject.save()
            
#         return redirect('home')
           

#     else:
       
#         form =  Newnotes()
#     return render(request,'newflash.html',{'newflash':form,})

