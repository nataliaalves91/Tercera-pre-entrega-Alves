from django.shortcuts import render
from .models import Teatro, Cine, Danza, Gastronomia, Avatar
from django.http import HttpResponse
from .forms import TeatroFormulario, CineFormulario, DanzaFormulario, GastronomiaFormulario, UserEditForm, AvatarFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required



def obras_teatro (req, nombre, genero, edad, fecha_estreno, autor):

    nueva_obra = Teatro(nombre=nombre, genero=genero, edad=edad)
    nueva_obra.save()
    return HttpResponse (f'<p>Nueva obra {nueva_obra.nombre}, apta a partir de {nueva_obra.edad} años, creada!</p>')

#Para poder hacer un listado de todas las obras disponibles, a través de los managers, creamos la función correspondiente para hacer una consulta a la BdD

def lista_obras(req):

    lista = Teatro.objects.all()

    return render(req, "lista_obras.html", {"lista_obras": lista})

#Definimos la renderización del resto de los templates

def inicio (req):

    try:
        avatar= Avatar.objects.get(user=req.user.id)
        return render(req, "pantalla_inicio.html", {"url": avatar.imagen.url})
    except:
        return render(req, "pantalla_inicio.html")

def about_me (req):

    return render(req, "aboutme.html", {})

def funcion_danza (req):

    return render(req, "funciones_danza.html", {})


def proyecciones (req):

    return render(req, "proyecciones.html", {})


def degustaciones (req):

    return render(req, "gastronomia.html", {})


#Creamos el primer formulario, para que se puedan crear nuevas obras de teatro



def teatro_formulario (req):


    if req.method == 'POST':

        miFormulario= TeatroFormulario(req.POST, req.FILES)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            
            nueva_obra = Teatro(nombre=data['título'], genero=data['género'], edad=data['edad_mínima'], imagen=data['imagen'])
            nueva_obra.save()

            return render(req, "creado_exito.html", {})
        
        else:
            return render(req, "pantalla_inicio.html", {"message": "Datos inválidos"})

    
    else:

        miFormulario= TeatroFormulario()
   
        return render(req, "teatro_formulario.html", {"FormuTeatro": miFormulario})
   
    
#Se crea la consulta

def busqueda_teatro (req):

    return render(req, "busqueda_teatro.html", {})


def buscar_teatro (req):

    if req.GET["obra_teatro"]:

        obra_teatro = req.GET["obra_teatro"]

        nombres = Teatro.objects.filter(nombre__icontains=obra_teatro)

        return render(req, "resultado_busqueda_teatro.html", {"obra_teatro": obra_teatro, "obras_teatro": nombres})
    
    else:
        return render(req, "pantalla_inicio.html", {})


#Se continúa con los formularios

def cine_formulario (req):


    if req.method == 'POST':

        miFormulario= CineFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            
            crear_funcion = Cine(nombre=data['nombre'], genero=data['genero'], edad_minima=data['edad_minima'])
            crear_funcion.save()

            return render(req, "creado_exito.html", {})
        
        else:
            return render(req, "pantalla_inicio.html", {"message": "Datos inválidos"})

    
    else:

        miFormulario= CineFormulario()
   
        return render(req, "cine_formulario.html", {"FormuCine": miFormulario})
    


##

def danza_formulario (req):

    if req.method == 'POST':

        miFormulario= DanzaFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            
            nueva_funcion = Danza(nombre=data['nombre'], edad=data['edad'], fecha=data['fecha'])
            nueva_funcion.save()

            return render(req, "creado_exito.html", {})
        
        else:
            return render(req, "pantalla_inicio.html", {"message": "Datos inválidos"})

    
    else:

        miFormulario= DanzaFormulario()
   
        return render(req, "danza_formulario.html", {"FormuDanza": miFormulario})


##

def gastronomia_formulario (req):

    if req.method == 'POST':

        miFormulario= GastronomiaFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            
            nuevo_local = Gastronomia(nombre=data['nombre'], localidad=data['localidad'], testeado=data['testeado'])
            nuevo_local.save()

            return render(req, "creado_exito.html", {})
        
        else:
            return render(req, "pantalla_inicio.html", {"message": "Datos inválidos"})

    
    else:

        miFormulario= GastronomiaFormulario()
   
        return render(req, "gastronomia_formulario.html", {"GastronomiaFormulario": miFormulario})
    


# creamos listados

def lista_danza (req):

    listado_danza = Danza.objects.all()

    return render (req, "lista_danza.html", {"listado_danza" : listado_danza})


def lista_cine (req):

    listado_cine = Cine.objects.all()

    return render (req, "lista_cine.html", {"listado_cine" : listado_cine})





#VBC

class GastronomiaList(ListView):

    model = Gastronomia
    template_name = 'gastronomia_list.html'
    context_object_name = 'locales_comida'



class GastronomiaDetail(DetailView):

    model = Gastronomia  
    template_name = 'gastronomia_detail.html'
    context_object_name = 'local_comida'


class GastronomiaCreate(CreateView):

    model = Gastronomia
    template_name = 'gastronomia_create.html'
    fields = ["nombre", "localidad", "testeado", "telefono", "apto_veganos"]
    success_url = "/gestion_cultural/"


class GastronomiaUpdate (LoginRequiredMixin, UpdateView):

    model = Gastronomia
    template_name = 'gastronomia_update.html'
    fields = ('__all__')
    success_url = "/gestion_cultural/lista-gastronomia/"
    context_object_name = 'detalle_gastronomia'



class GastronomiaDelete(LoginRequiredMixin, DeleteView):

    model = Gastronomia
    template_name = 'gastronomia_delete.html'
    success_url = "/gestion_cultural/"
    context_object_name = 'delete_gastronomia'


def login_view(req):

    if req.method == 'POST':

        miFormulario= AuthenticationForm(req, data=req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            
            username = data.get("username")
            password = data.get("password")

            user = authenticate(username=username, password=password)
            

            if user is not None:
                login(req, user)
                return render(req, "bienvenida.html", {"message": f"¡Bienvenido, {username}!"})
                
        
            else:
                return render(req, "pantalla_error.html", {"message": "Datos inválidos"})
            
        else:
            return render(req, "pantalla_error.html", {"message": "Datos inválidos"})
            
    else:

        miFormulario= AuthenticationForm()
   
        return render(req, "login.html", {"miFormulario": miFormulario})
    






# función de registro para que reciba req (get o post)

def register(req):


    if req.method == 'POST':

        miFormulario= UserCreationForm(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            
            user = data["username"]
            miFormulario.save()

            
            return render(req, "bienvenida.html", {"message": f" Usuario {user} creado con éxito, ¡bienvenido!"})
        
        else:
            return render(req, "pantalla_error.html", {"message": "Datos inválidos"})

    
    else:

        miFormulario= UserCreationForm()
   
        return render(req, "registro.html", {"miFormulario": miFormulario})
    
@login_required
def edita_perfil(req):

    usuario = req.user

    if req.method == 'POST':

        miFormulario= UserEditForm(req.POST, instance=req.user)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            
            usuario.first_name = data.get("first_name")
            usuario.last_name = data.get("last_name")
            usuario.email = data.get("email")
            usuario.set_password(data["password1"])
            usuario.save()
            
            return render(req, "bienvenida.html", {"message": "Usuario modificado con éxito"})
        
        else:
            return render(req, "editar_perfil.html", {"miFormulario": miFormulario})
            
    else:

        miFormulario= UserEditForm(instance=req.user)
   
        return render(req, "editar_perfil.html", {"miFormulario": miFormulario})
    

@staff_member_required
def agregar_avatar(req):


    if req.method == 'POST':

        miFormulario = AvatarFormulario(req.POST, req.FILES)


        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            avatar = Avatar(user = req.user, imagen = data['imagen'])
            avatar.save()
            
            

            return render (req, "creado_exito.html", {"message" : "Avatar creado correctamente"})

        else:
            return render (req, "pantalla_error.html", {"message" : "Datos inválidos"})
    
    else:

        miFormulario= AvatarFormulario()

        return render (req, "agregar_avatar.html", {"miFormulario" : miFormulario})
    
