from django.contrib import admin

from .models import Profile,Notes,Additionals,Subject
# Register your models here.

admin.site.register(Profile)
admin.site.register(Subject)
admin.site.register(Notes)
admin.site.register(Additionals)
