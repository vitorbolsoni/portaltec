from django.shortcuts import render
from .models import VidAssuntoVideo, VidVideo, FaqIndice, FaqQuestao, FaqResposta

# Create your views here.


def aprendizagem_index(request):
    return render(request, "central_aprendizagem/central_aprendizagem_index.html")


def video_aulas(request):
    lista_assunto = VidAssuntoVideo.objects.order_by('ds_assunto')
    lista_video = VidVideo.objects.all().order_by('posicao_video')
    context = {'lista_assunto': lista_assunto,
               'lista_video': lista_video}
    return render(request, "central_aprendizagem/central_aprendizagem_videos.html", context)


def faq(request):
    buscar = request.GET.get('buscar')

    if buscar:
        lista_resposta = FaqResposta.objects.order_by('posicao_resposta')
        lista_questao = FaqQuestao.objects.filter(ds_questao__icontains=buscar).order_by('posicao_questao')
        lista_indice = FaqIndice.objects.order_by('posicao_indice')

        context = {'lista_indice': lista_indice,
                   'lista_questao': lista_questao,
                   'lista_resposta': lista_resposta}

    else:
        lista_indice = FaqIndice.objects.order_by('posicao_indice')
        lista_questao = FaqQuestao.objects.order_by('posicao_questao')
        lista_resposta = FaqResposta.objects.order_by('posicao_resposta')

        context = {'lista_indice': lista_indice,
                   'lista_questao': lista_questao,
                   'lista_resposta': lista_resposta}

    return render(request, "central_aprendizagem/central_aprendizagem_faq.html", context)
