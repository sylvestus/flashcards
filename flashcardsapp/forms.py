from dataclasses import field
from .models import *
from django import forms

class UprofileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic','bio']

class NewsubjectForm(forms.ModelForm):
    class Meta:
        model=Subject
        exclude=['profile']

class Newnotes(forms.ModelForm):
    class Meta:
        model=Notes
        exclude=['profile','subject']

class newAdds(forms.ModelForm):
    class Meta:
        model=Additionals
        exclude=['profile','subject','notes']