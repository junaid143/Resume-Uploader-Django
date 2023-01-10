from django.contrib import admin
from .models import Resume

# Register your models here.
@admin.register(Resume)
class ResumeModel(admin.ModelAdmin):
    list_display = ['fname' ,'lname','dob','gender','language','locality','city','state' ,'pin','mobile','email','programming_language','profile_photo']
