from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from charity.models import Donations
from django.views.generic import ListView
import datetime
# Create your views here.

class HomeTemplateView(TemplateView):
    template_name = "charity/index.html"
    
    
    
class contactTemplateView(TemplateView):
    template_name = "charity/contact.html"
    
    def post(self, request):
            fname=request.POST.get("fname")
            mobile=request.POST.get("mobile")
            category=request.POST.get("donation")
            email=request.POST.get("address")
            message=request.POST.get("text")
        
            contact = Donations.objects.create(
                donor_name = fname,
                donor_mobile = mobile,
                Donation_type = category,
                donor_address = email,
                request = message,
            )
        
            contact.save()
        
            messages.add_message(request, messages.SUCCESS, f"Thank you {fname} for making a donation.")
            return  render(request, 'charity/contact.html')


class manageTemplateView(ListView):
    template_name = "charity/manage-donation.html"
    login_required = True
    model = Donations
    context_object_name = "donations"
    paginate_by = 3
    
    
    def get_context_data(self, *args , **kwargs):
        context = super().get_context_data(*args, **kwargs)
        donations = Donations.objects.all()
        context.update({
        "title":"Manage Donations"
        }
        )
        return context
    
    def post(self, request):
        #date = request.POST.get("date")
        donation_id = request.POST.get("donation-id")
        contact = Donations.objects.get(id=donation_id)
        contact.accepted=True
        contact.accepted_date = datetime.datetime.now()
        contact.save()
        
        messages.add_message(request, messages.SUCCESS, f"You accepted the donation of {contact.donor_name}")
        return HttpResponseRedirect(request.path)
        
        


    
class Donation(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category
        contact = Donations.objects.filter(
            category__name__contains='Donations')
        Food = Donation.objects.filter(category__name__contains='Food')
        Footware= Donation.objects.filter(category__name__contains='Footware')
        Clothes = Donation.objects.filter(category__name__contains='Clothes')
        Fund= Donation.objects.filter(category__name__contains='Fund')
        
        context = {
            'Donations': Donation,
           
            
            
            'Food': Food,
            'Footware' : Footware,
            'Clothes' : Clothes,
            'Fund': Fund,
        }
        return render(request, 'charity/index.html/Donations', context)