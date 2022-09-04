from django.contrib import admin

from .models import Symptoms, Profile, City, Vaccines, Masks

# Register your models here.
admin.site.register(Symptoms)
admin.site.register(Profile)
admin.site.register(City)
admin.site.register(Vaccines)
admin.site.register(Masks)