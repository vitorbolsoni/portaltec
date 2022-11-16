from django.urls import path
from . import views

urlpatterns = [
    # path('aplicativos_index', views.aplicativos_index, name='aplicativos_index'),
    path('dashboards', views.dashboards, name='dashboards'),
    path('bot_telegram', views.bot_telegram, name='bot_telegram')
]
