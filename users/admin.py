from django.contrib import admin
from .models import Profile

#allows for the model created to show on the Admin page
admin.site.register(Profile)
