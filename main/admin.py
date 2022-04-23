from django.contrib import admin
from .models import Payments,Roombookings,Rooms

# Register your models here.
admin.site.register(Payments)
admin.site.register(Roombookings)
admin.site.register(Rooms)
