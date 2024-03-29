from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from aulas.models import Aluno

# Create your views here. 
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    return render(request,"users/index.html",{
        "aluno":Aluno.objects.get(matricula=int(request.user.username))
    })

def login_view(request):
    if request.method=="POST":
        username= request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)  #se credenciais tao certas, devolve usuario
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("users:index"),{
                "aluno":Aluno.objects.get(matricula=int(user.username))
            })
        else:
            return render(request,"users/login.html",{
                "message":"Invalid user credentials"
            })
    return render(request,"users/login.html")

def logout_view(request):
    logout(request)
    return render(request,"users/login.html",{
        "message":"Logged Out"
    })
