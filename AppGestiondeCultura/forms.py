from django import forms 
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Avatar


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


class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text=" ",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    email = forms.EmailField(label= "Ingrese su correo: ")
    first_name = forms.CharField(label= "Nombre:")
    last_name = forms.CharField(label = "Apellido: ")
    imagen = forms.ImageField(label= "Avatar", required=False)

    class Meta:
        model=User  
        fields=["first_name", "last_name", "email", "imagen"]

    def clean_password2(self):

        print (self.cleaned_data)

        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            raise forms.ValidationError("Las contraseñas ingresadas no coinciden")
        
        else:
            return password2
        

class AvatarFormulario(forms.ModelForm):
    ...
    class Meta:
        model=Avatar
        fields=( 'imagen', )



# class UserEditForm(UserChangeForm):

#     password = forms.CharField(
#         help_text=" ",
#         widget=forms.HiddenInput(), required=False
#     )

#     password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
#     password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    
#     class Meta:
#         model=User  
#         fields=["first_name", "last_name", "email"]

#     def clean_password2(self):

#         print (self.cleaned_data)

#         password1 = self.cleaned_data["password1"]
#         password2 = self.cleaned_data["password2"]

#         if password1 != password2:
#             raise forms.ValidationError("Las contraseñas ingresadas no coinciden")
        
#         else:
#             return password2
        

# class AvatarFormulario(forms.ModelForm):
#     ...
#     class Meta:
#         model=Avatar
#         fields=( 'imagen', )