from django.shortcuts import render
from django import forms
from . models import Horario,Aluno,Aula,Sala
from django.db.models import Max
# Create your views here.

def index(request):
    return render(request, "aulas/index.html")

def inscricao(request,aluno_id):
    aluno=Aluno.objects.get(pk=aluno_id).all()
    horario_max=Horario.objects.aggregate(Max('numero'))
    return render(request,"aulas/inscricao.html",{
        "aluno":aluno,
        "numero_horarios":horario_max,
        "aulas":Aula.objects.exclude(vagas<=0).all(),
    })

def form(request,aluno_id):
    if request.method=="POST":
        aluno=aluno.objects.get(pk=aluno_id)
        aula=Aula.object.get(pk=int(request.POST["aula"]))
        aula.alunos.add(aluno)
        return HttpResponseRedirect(reverse("perfil",args=(aluno_id,)))
