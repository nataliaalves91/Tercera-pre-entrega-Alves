from django.urls import path
from AppGestiondeCultura.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    
    path('teatro/<nombre>/<genero>/<edad>', obras_teatro),
    path('' , inicio, name='Inicial'),
    path('lista_obras/' , lista_obras),
    path('funciones-danza' , funcion_danza, name='FuncionesBaile'),
    path('filmaciones/' , proyecciones, name='Proyecciones'),
    path('gastronomia-degustaciones/', degustaciones, name='Restaurantes'),

    path('teatro-formulario/', teatro_formulario, name='TeatroFormulario'), #crear nuevas obras
    path('busqueda-teatro/', busqueda_teatro, name='BusquedaTeatro'), #buscar obras
    path('buscar-teatro/', buscar_teatro, name='BuscarTeatro'), #trae la info de "buscar"

    path('cine-formulario/', cine_formulario, name='CineFormulario'),

    path('danza-formulario/', danza_formulario, name='DanzaFormulario'),

    path('gastronomia-formulario/', gastronomia_formulario, name='GastronomiaFormulario'),

    path('lista-danza/', lista_danza, name='ListaDanza'),
    
    path('lista-cine/', lista_cine, name='ListaCine'),

    path('lista-gastronomia/', GastronomiaList.as_view(), name='ListaGastronomia'),
    path('detalle-gastronomia/<pk>', GastronomiaDetail.as_view(), name='DetalleGastronomia'),
    path('crea-gastronomia/', GastronomiaCreate.as_view(), name='CreaGastronomia'),
    path('actualiza-gastronomia/<pk>', GastronomiaUpdate.as_view(), name='ActualizaGastronomia'),
    path('elimina-gastronomia/<pk>', GastronomiaDelete.as_view(), name='EliminaGastronomia'),
    path('login/', login_view, name='Login'),
    path('registrarse/', register, name='Registrar'),
    path('logout', LogoutView.as_view(template_name="logout.html"), name='Logout'),
  


    

    # path('eliminar-local/<int:id>', eliminar_local, name='EliminarGastronomia'),
    



    
]
