import geocoder

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm
import datetime
from .backEnd import FaceRecognition
from Etudiants.models import UserProfil, PresenceList


facerecognition = FaceRecognition()


# La fonction de connexion
def login_etudiant(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print('=' * 80)
        if user is not None:
            return redirect('Etudiants:dashboard')
        else:
            messages.error(request, 'Erreur d\'identification, veuillez réessayer')                                
            return render(request, 'login.html')
    
    return render(request, 'login.html')


# L'affichage du dashboard
def dashboard(request):
    return render(request, 'dashboard.html')


# La fonction de déconnexion
def sign_out(request):
    logout(request)
    return redirect('Etudiants:connexion')

# la fonction de capture du visage
def capture_face(request):
    return render(request, 'capture_face.html')

# reconnaissance faciale
def face_identify(request):
    face_id = facerecognition.recognizeFace()
    print(face_id)
    return redirect('welcome/' + str(face_id))

def register(request):

    if request.POST:
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Enregistrer avec succès!')
            addFace(request.POST['face_id'])
            return redirect('/')
        else:
            messages.error(request, "Echec enrégistrement!")

    form = RegisterForm()
    context = {
        'title' : 'Formulaire d\'enrégistrement',
        'form' : form
    }
    return render(request, 'register.html', context)


def addFace(face_id):
    face_id = face_id
    facerecognition.faceDetect(face_id)
    facerecognition.trainFace()
    return redirect('/')

def welcome(request, face_id):
    face_id = int(face_id)
    print(face_id)
    data = {
        'user': UserProfil.objects.get(face_id= face_id)
    }

    return render(request, 'app_profil', data)


# def capture_location(request):
#     if request.method == 'POST':
#         latitude = request.POST['latitude']
#         longitude = request.POST['longitude']
#         print(latitude, longitude)
#         g = geocoder.ip('me')
#         print(g.latlng)
#         return HttpResponse('ok')
#     return render(request, 'capture_location.html')

# def end_regis(request):
#     user = request.user
#     desactivate = False
#     try:
#         Etudiant = Etudiant.objects.get(user_id=user.id)
#         regis = Etudiant.register_set.select_for_update()[0]
#     except Etudiant.DoesNotExist:
#         pass
#     else:
#         if regis.end_time is None:
#             now = datetime.datetime.now().strftime('%H:%M:%S')  # Time like '23:12:05'
#             regis.end_time = now
#             regis.save()
#         else:
#             desactivate = True
#         return redirect(reverse('Etudiants:home'), {'desactivate': desactivate})




# def home(request):
#     locate = visitor_ip_address(request)
#     if locate:
#         print(locate)
#         return render(request, 'map.html', {'locate': locate})
#     else:
#         return HttpResponse("Vous n'êtes pas à la fabrique")


# def visitor_ip_address(request):
#     wifi_adress = '196.47.133.57'
#     g = geocoder.ip("me")
#     ip = g.geojson['features'][0]['properties']['ip']
#     print(ip)
#     if wifi_adress == ip:
#         loc = g.geojson['features'][0]['geometry']['coordinates']
#         return loc
#     else:
#         return None

def app_profil(request):
    return render(request, 'app-profile.html')


def email_verification(request):
    return render(request, 'email-read.html')


def page_list(request):
    return render(request, 'page-order-list.html')
