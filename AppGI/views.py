from django.shortcuts import render
from django.http import HttpResponse
from AppGI.models import Usuarios, e_abiss, e_adventure
from AppGI.forms import *


# Create your views here.

def inicio(request):

    return render(request, "AppGI/inicio.html")


def crear_usuario(request):

    if request.method == "POST":

        info_formulario = Usuarios_formulario(request.POST)

        if info_formulario.is_valid():

            info_dic = info_formulario.cleaned_data

            usuario_nuevo = Usuarios(
                usuario=info_dic["usuario"], 
                email=info_dic["email"],
                uids=info_dic["uids"],
                server=info_dic["server"]
                )
            
            usuario_nuevo.save()

            return render(request, "AppGI/inicio.html")
        
    else:
         
         info_formulario = Usuarios_formulario()

    return render(request, "AppGI/crear_usuario.html",{"formu": info_formulario})


def crear_e_adventure(request):

    if request.method == "POST":

        info_formulario = e_adventure_formulario(request.POST)

        if info_formulario.is_valid():

            info_dic = info_formulario.cleaned_data

            adventure_nuevo = e_adventure(
                pj_nombre=info_dic["pj_nombre"], 
                pj_elemento=info_dic["pj_elemento"],
                pj_lv=info_dic["pj_lv"]
                )
            
            adventure_nuevo.save()

            return render(request, "AppGI/inicio.html")
        
    else:
         
         info_formulario = e_adventure_formulario()

    return render(request, "AppGI/crear_e_adventure.html",{"formu": info_formulario})

def crear_e_abiss(request):

    if request.method == "POST":

        info_formulario = e_abiss_formulario(request.POST)

        if info_formulario.is_valid():

            info_dic = info_formulario.cleaned_data

            abiss_nuevo = e_abiss(
                pj_nombre=info_dic["pj_nombre"], 
                pj_elemento=info_dic["pj_elemento"],
                pj_lv=info_dic["pj_lv"],
                fecha_abismo=info_dic["fecha_abismo"],
                paso=info_dic["paso"]
                )
            
            abiss_nuevo.save()

            return render(request, "AppGI/inicio.html")
        
    else:
         
         info_formulario = e_abiss_formulario()

    return render(request, "AppGI/crear_e_abiss.html",{"formu": info_formulario})


def busqueda_usuario(request):
    
    return render(request, "AppGI/buscar_usuario.html")


def resultados_usuario(request):

    usuario = request.GET["usuario"]

    resultado = Usuarios.objects.filter(nombre__iexact = usuario)

    return render(request, "AppGI/resultados.html", {"resultado":resultado})
