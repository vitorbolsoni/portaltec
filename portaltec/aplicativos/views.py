from django.shortcuts import render
from .models import Dashboard

# Create your views here.


# def aplicativos_index(request):
#     return render(request, "aplicativos/aplicativos_index.html")


def dashboards(request):
    lista_dashboard = Dashboard.objects.order_by('ds_dashboard')
    context = {'lista_dashboard': lista_dashboard}
    return render(request, "aplicativos/aplicativos_dashboards_index.html", context)


def bot_telegram(request):
    return render(request, "aplicativos/bot_hunoc_index.html")
