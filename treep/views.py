from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView,TemplateView,CreateView,FormView, DeleteView
from .models import Roteiro,Natureza,Gastronomia,Praia,Cultura
from .forms import RoteiroForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout as logout_django
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required




class indexView(TemplateView):
    template_name = "treep/index.html"
    
    def get(self, request):
        natureza = Natureza.objects.all()
        praia = Praia.objects.all()
        gastronomia = Gastronomia.objects.all()
        cultura = Cultura.objects.all()
       
        context = {
            "praia":praia,
            "gastronomia":gastronomia,
            "natureza":natureza,
            "cultura":cultura,
            

        }
        return render(request, self.template_name,context)

class RoteiroCreate(FormView):
    model = Roteiro
    
    form = RoteiroForm()
    template_name = "treep/criar.html"
    success_url = "/thanks/"


class RoteiroDelete(DeleteView):
    model = Roteiro
    success_url = "/"
    template_name = "treep/roteiroDelete.html"


@login_required(login_url="/login")
def Create(request):
    form = RoteiroForm()
    if request.method == 'GET':
        roteiro = Roteiro.objects.all()
        form = RoteiroForm()
        context ={
            'roteiro':roteiro,
            'form':form,
        }
        return render(request, "treep/criar.html", context)

    elif request.method == 'POST':
        form = RoteiroForm(request.POST)
        if form.is_valid():
            form.instance.usuario = request.user
            form.save()
            return redirect('/')
            
        else:
            print("realmente n erou")
            return HttpResponse('Teste de erro')
    return render(request, "treep/criar.html", {"form":form})


#mudar a lista
#acho que o react que faz isso, mas vou deixar uma listagem padrão

"""class RoteiroList(ListView):
   
    template_name = "treep/roteiro.html"
    queryset = Roteiro.objects.all()"""
@login_required(login_url="/login")
def RoteiroList(request):
    roteiros = Roteiro.objects.filter(usuario=request.user)
    return render(request,"treep/roteiro.html",{"roteiros":roteiros})
    

def cadastro(request):
    if request.method == "GET":
        return render(request,'treep/cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username)

        if (user):
            return HttpResponse('ESSE USUARIO JA EXISTE!')
        user = User.objects.create_user(username=username,email=email,password=senha)
        user.save()

        return redirect("/login")

def login(request):
    if request.method == "GET":
        
        return render(request,"treep/login.html")
    else:
        username = request.POST.get("username")
        senha = request.POST.get("senha")

        user = authenticate(username=username, password=senha)

        if (user):
            login_django(request,user)
            return redirect("/")
        else:
            return HttpResponse("Email ou senha inválido")
@login_required        
def logout(request):
    logout_django(request)
    return redirect("/")
