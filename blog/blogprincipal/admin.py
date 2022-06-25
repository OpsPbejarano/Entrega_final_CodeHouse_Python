from django.contrib import admin
from blogprincipal.models import *

class BlogAdmin(admin.ModelAdmin):
    list_display = ("titulo","descripcion","contenido","autor")

admin.site.register(Blog,BlogAdmin)
