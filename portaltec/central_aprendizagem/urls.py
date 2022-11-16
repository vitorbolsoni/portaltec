from django.urls import path
from . import views

urlpatterns = [
    path('', views.aprendizagem_index, name='central_aprendizagem'),
    path('video_aulas', views.video_aulas, name='video_aulas'),
    path('faq', views.faq, name='faq')
]
