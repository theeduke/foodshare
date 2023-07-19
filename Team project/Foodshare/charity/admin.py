from django.contrib import admin
from .models import Donations, Category

# Register your models here.
admin.site.register(Donations)
admin.site.register(Category)