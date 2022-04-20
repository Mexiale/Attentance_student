from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib import admin

from Etudiants.models import UserProfil, PresenceList


@admin.register(UserProfil)
class UserProfilAdmin(admin.ModelAdmin):
    list_display = ('user', 
                    'adresse',
                     'formation', 
                     'debut_formation', 
                     'fin_formation', 
                     'tel'
                     )

@admin.register(PresenceList)
class PresenceListAdmin(admin.ModelAdmin):
    
    list_display = ('etudiant', 
                    'Today' ,
                    'begin_time', 
                    'end_time')

