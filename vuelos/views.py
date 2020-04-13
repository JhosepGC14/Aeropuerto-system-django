from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import *


def index(request):
    context = {
        "vuelos": Vuelo.objects.all()
    }
    return render(request, "index.html", context)


def vuelo(request, vuelo_id):
    try:
        vuelo = Vuelo.objects.get(pk=vuelo_id)
    except Vuelo.DoesNotExist:
        raise Http404("Vuelo no existe")
    context = {
        "vuelo": vuelo,
        "pasajero": vuelo.pasajeros.all()
    }
    return render(request, "vuelo.html", context)

def reservar(request, vuelo_id):
    try:
        pasajero_id = int(request.POST["pasajero"])
        pasajero = Pasajero.objects.get(pk=pasajero_id)
        vuelo = Vuelo.objects.get(pk=vuelo_id)
    except KeyError:
        return render(request, "error.html", {"msg": "No Selecciono Pasajero"})
    except Vuelo.DoesNotExist:
        return render(request, "error.html", {"msg": "No Existe el Vuelo"})
    except Pasajero.DoesNotExist:
        return render(request, "error.html", {"msg": "No Existe pasajero"})
    pasajero.vuelo.add(vuelo)
    
