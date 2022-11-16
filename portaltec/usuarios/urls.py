from django.urls import path
from . import views

urlpatterns = [
    path('logon', views.logon, name='logon'),
    path('aplicativos_index', views.aplicativos_index, name='aplicativos_index'),
    path('logoff', views.logoff, name='logoff'),
]
