from django.db import models
from django.contrib.auth.models import Group
from tinymce import models as tinymce_models

# Create your models here.


class VidAssuntoVideo(models.Model):
    grupo_usuario = models.ForeignKey(Group, on_delete=models.PROTECT)
    posicao_assunto = models.IntegerField(default=0)
    ds_assunto = models.CharField(max_length=40)
    dt_cadastro = models.DateTimeField(auto_now=True)

    def clean(self):
        self.ds_assunto = str(self.ds_assunto.title())

    def __str__(self):
        return self.ds_assunto


class VidVideo(models.Model):
    assunto = models.ForeignKey(VidAssuntoVideo, on_delete=models.PROTECT)
    posicao_video = models.IntegerField(default=0)
    dir_video = models.FileField(upload_to="video")
    ds_video = models.CharField(max_length=40)
    dt_cadastro = models.DateTimeField(auto_now=True)

    def clean(self):
        self.ds_video = str(self.ds_video.title())

    def __str__(self):
        return self.ds_video


class FaqIndice(models.Model):
    grupo_usuario = models.ForeignKey(Group, on_delete=models.PROTECT)
    posicao_indice = models.IntegerField(default=0)
    ds_indice = models.CharField(max_length=40)
    dt_cadastro = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ds_indice


class FaqQuestao(models.Model):
    indice = models.ForeignKey(FaqIndice, on_delete=models.PROTECT)
    posicao_questao = models.IntegerField(default=0)
    ds_questao = models.CharField(max_length=100)
    dt_cadastro = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ds_questao


class FaqResposta(models.Model):
    questao = models.ForeignKey(FaqQuestao, on_delete=models.PROTECT)
    posicao_resposta = models.IntegerField(default=0)
    ds_resposta = tinymce_models.HTMLField(max_length=2200)
    dt_cadastro = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.posicao_resposta}º resposta'
