from django.urls import path
from AppGestiondeCultura.views import *


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

    path('lista-musica/', MusicaList.as_view(), name='ListaMusica'),
    path('detalle-musica/<pk>', MusicaDetail.as_view(), name='DetalleMusica'),
    path('crea-musica/', MusicaCreate.as_view(), name='CreaMusica'),
    path('actualiza-musica/<pk>', MusicaUpdate.as_view(), name='ActualizaMusica'),
    path('elimina-musica/<pk>', MusicaDelete.as_view, name='EliminaMusica'),



    
]
