from django.urls import path
from Etudiants import views

app_name = 'Etudiants'
urlpatterns = [
    path('', views.login_etudiant, name='connexion'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('face_identify/', views.face_identify, name='face_identify'),
    path('deconnexion/', views.sign_out, name='deconnexion'),
    path('emager/', views.capture_face, name='emager'),
    path('app_profil/', views.app_profil, name='app_profil'),
    path('email_verification/', views.email_verification, name='email_verification'),
    path('page_list/', views.page_list, name='page_list'),
]
