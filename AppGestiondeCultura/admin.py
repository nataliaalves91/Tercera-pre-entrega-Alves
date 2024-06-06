from django.contrib import admin
from .models import Danza, Teatro, Cine, Gastronomia

# Register your models here.
admin.site.register (Danza)
admin.site.register (Teatro)
admin.site.register (Cine)
admin.site.register (Gastronomia)