from django.shortcuts import render, redirect
from .models import Generos, Historia, Upgrade

from .forms import GeneroForm, HistoriaForm

# Create your views here.

def home(request):
  generos = Generos.objects.all()
  historia = Historia.objects.all()[:5]
  continuacao = Historia.objects.all()[5:7]
  upgradesTopo = Upgrade.objects.all()[:5]
  upgradesMeio = Upgrade.objects.all()[5:10]
  upgradesBaixo = Upgrade.objects.all()[10:15]

  dosUsuarios = Historia.objects.all()[7:]
  
  context = {
    "generos" : generos,
    "historia" : historia,
    "continuacao" : continuacao,
    "upgradesTopo" : upgradesTopo,
    "upgradesMeio" : upgradesMeio,
    "upgradesBaixo" : upgradesBaixo,
    "dosUsuarios" : dosUsuarios,
  }
  
  return render(request,"home.html", context=context)



def formGenero(request):
  
  generos = Generos.objects.all()

  context ={
    "generos" : generos,
  }
  return render(request,"todosGeneros.html", context)


def formGeneroAdd(request):
    context ={}
    form = GeneroForm(request.POST or None, request.FILES or None)
    if form.is_valid() and request.method=="POST":
        form.save()
        return redirect("/")
 
    context['form']= form
    return render(request, "form.html", context)


def formGeneroEdit(request, id):
    context ={}
    genero = Generos.objects.get(id=id)
    form = GeneroForm(request.POST or None, instance = genero)
    if form.is_valid() and request.method=="POST":
        form.save()
        return redirect("/")
    context['form']= form
    return render(request, "form.html", context)


def formGeneroRemove(request, id):
  genero = Generos.objects.get(id=id)
  context={
    "item" : genero,
  }
  if request.method == "POST":
    if "confirm" in request.POST:
      genero.delete()

    return redirect("/")
  return render(request, "confirmacao.html", context=context)


def formHistoria(request):

  historiasFixas = Historia.objects.all()[:7]
  historiasUsuarios = Historia.objects.all()[7:]

  context ={
    "historiasFixas" : historiasFixas,
    "historiasUsuarios" : historiasUsuarios
  }
  return render(request,"todasHistorias.html", context=context)


def formHistoriaAdd(request):
    context ={}
    form = HistoriaForm(request.POST or None, request.FILES or None)
    if form.is_valid() and request.method=="POST":
        form.save()
        return redirect("/")
 
    context['form']= form
    return render(request, "form.html", context)


def formHistoriaEdit(request, id):
    context ={}
    historia = Historia.objects.get(id=id)
    form = HistoriaForm(request.POST or None, instance = historia)
    if form.is_valid() and request.method=="POST":
        form.save()
        return redirect("/")
    context['form']= form
    return render(request, "form.html", context)


def formHistoriaRemove(request, id):
  historia = Historia.objects.get(id=id)
  context={
    "item" : historia,
  }
  if request.method == "POST":
    if "confirm" in request.POST:
      historia.delete()

    return redirect("/")
  return render(request, "confirmacao.html", context=context)


def alteracoes(request):
  return render(request,"alteracoes.html")