
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default="")
    profile_pic = CloudinaryField('images')
    bio = models.TextField()
    contact=models.CharField(max_length=300)

    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()

    def update_profile(cls,id):
        Subject.objects.get(user_id=id) 

    def __str__(self):
        return self.user.username

class Subject(models.Model):
    subjectname=models.CharField(max_length=50)
    date_posted=models.DateTimeField(default=timezone.now)
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE,default="",null=True)
    def __str__(self):
        return self.subjectname

    def save_subject(self):
        self.save()
        
    def delete_subject(self):
        self.delete()
        
    def edit_subject(self,new_subject):
        self.subjectname = new_subject
        self.save()    



class Notes(models.Model):
    notes_title=models.CharField(max_length=100)
    notes=models.TextField()
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE,default="",null=True)
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE,default="",null=True)

    def __str__(self):
        return self.notes_title

    def save_notes(self):
        self.save()
        
    def delete_notes(self):
        self.delete()
        
    def edit_notes(self,new_notes):
        self.notes = new_notes
        self.save()    




class Additionals(models.Model):
    user_adds=models.TextField()
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE,default="",null=True)
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE,default="",null=True)
    notes=models.ForeignKey(Notes, on_delete=models.CASCADE,default="",null=True)
    def __str__(self):
        return self.user_adds


    def save_additionals(self):
        self.save()
        
    
        
      


        
