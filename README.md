# Preentrega3
##Pasos
Tener instalado 
- django 5.0.3 
- python 3.11
- vsc 1.87.0

Comentario: Se ha creado el archivo mediante django, con startproyect, pararse en la carpeta correspondiente con el cd PE_3 y luego con colocar la App a través de python manage.py startapp
Se ha tomato un template de start bootstrap. Para los templates, se a usado el padre para crear herencia para las otras plantillas.
Arrastrar la carpeta al vsc y comenzamos:

1. python manage.py makemigrations para poder crear las tablas de las class en la db
2. Luego se hace el python manage.py migrate
3. Instalar un visor de sqlite Viewer 
4. ir a la terminal y correr el python manage.py runserver para ver el server
5. ctrl+C para cerrar el server

Las clases son
-class Usuarios 
    usuario
    email 
    uids 
    server
    
-class e_adventure 
   pj_nombre
   pj_elemento
   pj_lv 
   
class e_abiss
   pj_nombre
   pj_elemento
   pj_lv
   fecha_abismo
   paso


Los URLS son
1. inicio= http://127.0.0.1:8000/AGI/
2. crear usuario= http://127.0.0.1:8000/AGI/crear_usuario
3. Crear el equipo de aventura= http://127.0.0.1:8000/AGI/crear_e_adventure
4. Crear el equipo de Abismo= http://127.0.0.1:8000/AGI/crear_e_abiss
5. Buscar usuario= http://127.0.0.1:8000/AGI/buscar_usuario
6. Ver resultados= http://127.0.0.1:8000/AGI/resultados  (esta aprte del codigo no funciona, tira un error en la funcion de filter que no he podido solucionar)
