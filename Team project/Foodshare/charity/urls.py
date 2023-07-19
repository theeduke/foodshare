from django.urls import path
from .views import HomeTemplateView, Donation, contactTemplateView, manageTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('Donation/', Donation.as_view(), name='Donation'),
    path('make-contact/', contactTemplateView.as_view(), name='Contacts'),
    path('manage-appointments/', manageTemplateView.as_view(), name='manage'),
]
