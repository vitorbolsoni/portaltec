from django.db import models
from django.contrib.auth.models import Group

# Create your models here.


class Dashboard(models.Model):
    grupo_usuario = models.ForeignKey(Group, on_delete=models.PROTECT)
    dir_dashboard = models.URLField(max_length=255)
    ds_dashboard = models.CharField(max_length=40)
    dt_cadastro = models.DateTimeField(auto_now=True)

    def clean(self):
        self.ds_dashboard = str(self.ds_dashboard.title())

    def __str__(self):
        return self.ds_dashboard
