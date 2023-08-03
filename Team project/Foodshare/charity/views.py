from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from charity.models import Donations
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .forms import  Form
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
                donor_email = email,
                request = message,
            )
        
            contact.save()
        
            messages.add_message(request, messages.SUCCESS, f"Thank you {fname} for making a donation.")
            return  render(request, 'charity/contact.html')
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'charity/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'charity/profile.html')

def Form(request):
  if request.method == "POST":
    form = Form(request.POST)
    if form.is_valid():
      form.save()
    else:
      form = form()
  return render(request, 'Charity/Form', {'form': form})

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
        donation_id = request.POST.get("donation-id")
        contact = Donations.objects.get(id=donation_id)
        contact.accepted=True
        contact.accepted_date = datetime.datetime.now()
        contact.save()
        
        messages.add_message(request, messages.SUCCESS, f"You accepted the donation of {contact.donor_name}")
        return HttpResponseRedirect(request.path)