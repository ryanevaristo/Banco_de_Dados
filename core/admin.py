from django.contrib import admin

# Register your models here.
from core.models import Participante, Empresa
@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ['id','Nome','cpf']
admin.site.register(Empresa)


