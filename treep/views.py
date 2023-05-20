from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from django.http import HttpResponse
from .models import Roteiro


# Create your views here.


"""def index(request):
    return HttpResponse("<a href='roteiro'>333333</a>")"""

class indexView(TemplateView):
    template_name = "treep/index.html"

class RoteiroList(ListView):
    meta = Roteiro
    #queryset = Roteiro.objects.all()
    template_name = "treep/roteiro.html"
    
    

    def get_queryset(self):
        
        x = self.request.GET.get('dias')
        
        
        print(f"Print do X {x}")

        if x == None:
            x = self.request.GET.get('dias')
            
            
            #print("30902399320923")
        else:
            #print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
            x = int(x)
        if self.request.GET.get('choice') == '1':
            #l = self.request.GET.get('choice')
            a = Roteiro.objects.order_by('nome')[:x]
            print("11111BANANA")
           # print(l)
        elif self.request.GET.get('choice') == '2':
            a = Roteiro.objects.order_by('id')[:x]
            #l = self.request.GET.get('choice')
            #if(l == '2'):
            #    print("Deu certo!")
            print("OVO")
            #print(l)
        elif self.request.GET.get('choice') == '3':
            a = Roteiro.objects.order_by('posicao')[:x]
        else:
            a = Roteiro.objects.all()[:x]
       


        return a
    
