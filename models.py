from re import A
from tabnanny import verbose
from unicodedata import name
from django.contrib.auth.models import User
from django.db import models


class UserProfil(models.Model):

    # user = models.OneToOneField(User, on_delete=models.CASCADE, max_length = 30)
    face_id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    adresse = models.CharField(max_length = 35, default=' ', blank=True, null=True)
    FORMATION = models.TextChoices('Référent Digital', 'Développeur IA' )
    formation = models.CharField(blank=True ,max_length = 25, choices=FORMATION.choices )
    debut_formation = models.DateTimeField(verbose_name="Date de début", auto_now=False, auto_now_add=False)
    fin_formation = models.DateTimeField(verbose_name="Date de Fin", auto_now=False, auto_now_add=False)
    tel = models.CharField(max_length =  30, default=' ', blank=True, null=True)
    bio = models.CharField(max_length = 200, default=' ', blank=True, null=True)
    image=models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.user.username + " (" + self.user.first_name + " " + self.user.last_name + ")"

    class Meta:
        verbose_name = 'Profils Etudiant'

class PresenceList(models.Model):

    etudiant = models.ForeignKey(UserProfil, on_delete=models.CASCADE)
    Today = models.DateField(verbose_name= "Date" ,auto_now=True)
    begin_time = models.TimeField(verbose_name="Heure d'arrivée", auto_now=False, auto_now_add=True)
    end_time = models.TimeField(verbose_name="Heure de départ", auto_now=False,  auto_now_add=True)

    def __str__(self):
        return self.etudiant.user.username

    class Meta:
        verbose_name = 'Presence List'
        verbose_name_plural = 'Liste de Presences'


# # class Register(models.Model):
#     Etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
#     date = models.DateField(verbose_name="Date du jour", auto_now=True)
#     departure_time = models.TimeField(verbose_name="Heure d'arrivée", auto_now=True, blank=True, null=True)
#     end_time = models.TimeField(verbose_name="Heure de départ", blank=True, null=True)

#     def __str__(self):
#         return self.Etudiant.user.username
