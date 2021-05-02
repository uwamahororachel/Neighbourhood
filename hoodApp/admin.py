from django.contrib import admin
from django.contrib import admin
from .models import Neighborhood,Profile,Business,Alert

# Register your models here.
admin.site.register(Neighborhood)
admin.site.register(Alert)
admin.site.register(Profile)
admin.site.register(Business)
