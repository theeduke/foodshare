from django.urls import path
from .views import HomeTemplateView, contactTemplateView, manageTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('make-contact/', contactTemplateView.as_view(), name='Contacts'),
    path('manage-appointments/', manageTemplateView.as_view(), name='manage'),
]
