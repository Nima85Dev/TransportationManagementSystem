from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('profile/', views.profileView, name='profile'),
    path('profile/register/', views.profileRegisterView, name='profile_register'),
    path('profile/edit/', views.ProfileEditView, name='profile_edit'),
    path('change-password/', views.changePasswordView, name='change_password'),
]
