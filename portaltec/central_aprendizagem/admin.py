from django.contrib import admin

# Register your models here.
from .models import FaqIndice, FaqQuestao, FaqResposta, VidAssuntoVideo, VidVideo

# admin.site.register([VidAssuntoVideo, VidVideo])

# admin.site.register([FaqIndice, FaqQuestao, FaqResposta])


@admin.register(VidAssuntoVideo)
class VidAssuntoVideoModelAdmin(admin.ModelAdmin):
    list_display = ['ds_assunto', 'posicao_assunto']
    ordering = ['posicao_assunto']
    search_fields = ['ds_assunto__icontains', 'posicao_assunto__icontains']


@admin.register(VidVideo)
class VidVideoModelAdmin(admin.ModelAdmin):
    list_display = ['ds_video', 'posicao_video', 'assunto']
    ordering = ['assunto', 'posicao_video']
    search_fields = ['ds_video__icontains', 'posicao_video__icontains', 'assunto__ds_assunto']


@admin.register(FaqIndice)
class FaqIndiceModelAdmin(admin.ModelAdmin):
    list_display = ['ds_indice', 'posicao_indice']
    ordering = ['posicao_indice']
    search_fields = ['ds_indice__icontains', 'posicao_indice__icontains']


@admin.register(FaqQuestao)
class FaqQuestaoModelAdmin(admin.ModelAdmin):
    list_display = ['ds_questao', 'posicao_questao', 'indice']
    ordering = ['indice', 'posicao_questao']
    search_fields = ['ds_questao__icontains', 'posicao_questao__icontains', 'indice__ds_indice']


@admin.register(FaqResposta)
class FaqRespostaModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'questao']
    ordering = ['questao', 'posicao_resposta']
    search_fields = ['questao__ds_questao', 'ds_resposta__icontains']
