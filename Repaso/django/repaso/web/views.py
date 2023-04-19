from django.shortcuts import render
from persona.models import Persona
# Create your views here.

def index(request):
    personas = Persona.objects.order_by('id')
    return render(request, 'index.html', {'personas':personas})