from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Olá mundo.')

def results(request, container_id):
    return HttpResponse(f'Resultado: {container_id}.')