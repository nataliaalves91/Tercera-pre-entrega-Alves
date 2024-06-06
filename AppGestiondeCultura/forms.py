from django import forms  

class TeatroFormulario(forms.Form):

    título= forms.CharField()
    género= forms.CharField()
    edad_mínima= forms.IntegerField()


class CineFormulario(forms.Form):

    nombre= forms.CharField()
    genero= forms.CharField()
    edad_minima= forms.IntegerField()


class DanzaFormulario(forms.Form):

    nombre= forms.CharField()
    edad= forms.IntegerField()
    fecha= forms.DateField()



class GastronomiaFormulario(forms.Form):

    nombre= forms.CharField()
    localidad = forms.CharField()
    testeado = forms.BooleanField()


