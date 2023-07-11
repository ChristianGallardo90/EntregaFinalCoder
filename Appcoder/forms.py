from django import forms
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User

class formSetEstudiante(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()    

class formSetCursos(forms.Form):
    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()

class formSetProfesor(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)    

class UserEditForm(UserChangeForm):
    username = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Username"}))
    email = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Email"}))
    first_name = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Firts Name"}))
    last_name = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Last Name"}))
    

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name' ]
        help_text = {k:"" for k in fields}

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="", widget= forms.PasswordInput(attrs={"placeholder":"Old Password"}))
    new_password1 = forms.CharField(label="", widget= forms.PasswordInput(attrs={"placeholder":"New Password"}))
    new_password2 = forms.CharField(label="", widget= forms.PasswordInput(attrs={"placeholder":"Confirmation new password"}))

    class Meta:
        model = User
        fields = ['old_password','old_password1','old_password2']
        help_text = {k:"" for k in fields}

class AvatarForm(forms.Form):
    avatar = forms.ImageField()