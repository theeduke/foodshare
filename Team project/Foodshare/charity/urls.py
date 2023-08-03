from django.urls import path
from .views import HomeTemplateView, contactTemplateView, manageTemplateView
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('make-contact/', contactTemplateView.as_view(), name='Contacts'),
    path('manage-appointments/', manageTemplateView.as_view(), name='manage'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('Form/', views.profile, name='Form'),
    path('login/', auth_view.LoginView.as_view(template_name='charity/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='charity/logout.html'), name="logout"),
]
