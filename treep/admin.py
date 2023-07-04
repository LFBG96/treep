from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Natureza)
admin.site.register(Gastronomia)
admin.site.register(Praia)
admin.site.register(Cultura)

#admin.site.register(Roteiro)

from django.db import models
from django.contrib import admin
from django.forms import CheckboxSelectMultiple

class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
admin.site.register(Roteiro,MyModelAdmin)
