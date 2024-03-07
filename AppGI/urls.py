from django.urls import path
from AppGI.views import *


urlpatterns = [
    path("", inicio, name="inicio"),
    path("crear_usuario", crear_usuario, name="crear_usuario"),
    path("crear_e_adventure", crear_e_adventure, name="crear_e_adventure"),
    path("crear_e_abiss", crear_e_abiss, name="crear_e_abiss"),
    path("buscar_usuario", busqueda_usuario),
    path("resultados", resultados_usuario)
]