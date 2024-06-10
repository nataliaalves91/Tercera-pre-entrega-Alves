from django.shortcuts import render
from .models import Teatro, Cine, Danza, Gastronomia
from django.http import HttpResponse
from .forms import TeatroFormulario, CineFormulario, DanzaFormulario, GastronomiaFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView



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

    return render(req, "pantalla_inicio.html", {})


def funcion_danza (req):

    return render(req, "funciones_danza.html", {})


def proyecciones (req):

    return render(req, "proyecciones.html", {})


def degustaciones (req):

    return render(req, "gastronomia.html", {})


#Creamos el primer formulario, para que se puedan crear nuevas obras de teatro



def teatro_formulario (req):

    print ('method: ', req.method)
    print ('POST: ', req.POST)

    if req.method == 'POST':

        miFormulario= TeatroFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            
            nueva_obra = Teatro(nombre=data['título'], genero=data['género'], edad=data['edad_mínima'])
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
    fields = ["nombre", "localidad", "testeado"]
    success_url = "/AppGestiondeCultura/"


class GastronomiaUpdate (UpdateView):

    model = Gastronomia
    template_name = 'gastronomia_update.html'
    fields = ('__all__')
    success_url = "/AppGestiondeCultura/"
    context_object_name = 'detalle_gastronomia'


class GastronomiaDelete(DeleteView):

    model = Gastronomia
    template_name = 'gastronomia_delete.html'
    success_url = "/AppGestiondeCultura/"
