from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from core.models import Evento


def evento(request, evento):
    e = Evento.get(evento=evento)
    return HttpResponse('{}', format(e))

'''
def index(request):
    return redirect('/agenda/')
'''



def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
