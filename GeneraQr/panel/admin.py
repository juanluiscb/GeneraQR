from django.contrib import admin
from panel.models import Lista

class ListaAdmin(admin.ModelAdmin):
  list_display = ('id','nombre','curso',)

admin.site.register(Lista)