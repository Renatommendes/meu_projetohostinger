from django.shortcuts import render
from .models import Estacao

def map_view(request):
    estacoes = Estacao.objects.all()
    return render(request, 'mapapp/map.html', {'estacoes': estacoes, 'api_key': 'AIzaSyCKyeLfN3GjEiDsYafdQGymklU-7VcKC6I'})




