from django.shortcuts import render
from django.http import HttpResponse
from Appcoder.models import Estudiante,Curso,Profesor,Avatar
from Appcoder.forms import formSetEstudiante,formSetCursos,formSetProfesor,UserEditForm,ChangePasswordForm,AvatarForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required
def inicio(request):
     avatar = getavatar(request)
     return render(request,"AppCoder/inicio.html",{"avatar": avatar})
@login_required
def cursos(request):
    return render(request,"AppCoder/cursos.html")
@login_required
def profesores(request):
    return render(request,"AppCoder/profesores.html")
@login_required
def estudiantes(request):
    return render(request,"AppCoder/estudiantes.html")
@login_required
def entregables(request):
    return render(request,"AppCoder/entregables.html")
@login_required
def setEstudiantes(request):
    Estudiantes = Estudiante.objects.all()
       
    if request.method == 'POST':
        miFormulario = formSetEstudiante(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            estudiantes = Estudiante(nombre=data["nombre"],apellido=data["apellido"],email=data["email"])
            estudiantes.save()
            miFormulario = formSetEstudiante()
            return render(request,"AppCoder/setEstudiantes.html",{"miFormulario":miFormulario,"Estudiantes": Estudiantes})

    else:
        miFormulario = formSetEstudiante
    return render(request,"AppCoder/setEstudiantes.html",{"miFormulario":miFormulario,"Estudiantes": Estudiantes})
@login_required
def getEstudiantes(request):
    return render(request,"AppCoder/getEstudiantes.html")
@login_required
def buscarEstudiante(request):
    if request.GET["nombre"]:
         nombre = request.GET["nombre"]
         estudiantes = Estudiante.objects.filter(nombre = nombre)
         return render(request,"AppCoder/getEstudiantes.html",{"estudiantes":estudiantes})
    else:
        respuesta = "no se enviaron datos"
    return HttpResponse(respuesta)
@login_required
def setCursos(request):
    if request.method == 'POST':
        miFormulario = formSetCursos(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            cursos = Curso(nombre=data["nombre"],camada=data["camada"])
            cursos.save()
            return render(request,"AppCoder/inicio.html")
    else:
          miFormulario = formSetCursos
    return render(request,"AppCoder/setCursos.html",{"miFormulario":miFormulario})      
@login_required   
def getCursos(request):
    return render(request,"AppCoder/getCursos.html")   
@login_required
def buscarCursos(request):
    if request.GET["nombre"]:
         nombre = request.GET["nombre"]
         cursos = Curso.objects.filter(nombre = nombre)
         return render(request,"AppCoder/getCursos.html",{"cursos":cursos})
    else:
        respuesta = "no se enviaron datos"
    return HttpResponse(respuesta)     
@login_required
def setProfesores(request):
    if request.method == 'POST':
        miFormulario = formSetProfesor(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            profesores = Profesor(nombre=data["nombre"],apellido=data["apellido"],email=data["email"],profesion=data["profesion"])
            profesores.save()
            return render(request,"AppCoder/inicio.html")
    else:
          miFormulario = formSetProfesor
    return render(request,"AppCoder/setProfesores.html",{"miFormulario":miFormulario})  
@login_required
def getProfesores(request):
    return render(request,"AppCoder/getProfesores.html")  
@login_required
def buscarProfesores(request):
    if request.GET["nombre"]:
         nombre = request.GET["nombre"]
         profesores = Profesor.objects.filter(nombre = nombre)
         return render(request,"AppCoder/getProfesores.html",{"profesores":profesores})
    else:
        respuesta = "no se enviaron datos"
    return HttpResponse(respuesta)     
@login_required  
def leerEstudiantes(request):
    Estudiantes = Estudiante.objects.all()
    return render (request, "Appcoder/setEstudiantes.html",{"Estudiantes":Estudiantes})
@login_required
def eliminarEstudiante(request,nombre_estudiante):
    estudiante = Estudiante.objects.get(nombre = nombre_estudiante)
    estudiante.delete()
    miFormulario = formSetEstudiante()
    Estudiantes = Estudiante.objects.all()
    return render (request, "Appcoder/setEstudiantes.html",{"miFormulario":miFormulario, "Estudiantes":Estudiantes})
@login_required
def editarEstudiante(request, nombre_estudiante):
    estudiante = Estudiante.objects.get(nombre = nombre_estudiante)
    if request.method == 'POST':
       
       miFormulario = formSetEstudiante(request.POST)
       if miFormulario.is_valid():
           data = miFormulario.cleaned_data

           estudiante.nombre = data['nombre']
           estudiante.apellido = data['apellido']
           estudiante.email = data['email']
           estudiante.save()
           miFormulario = formSetEstudiante()
           Estudiantes = Estudiante.objects.all()
           
           return render(request,"AppCoder/setEstudiantes.html",{"miFormulario":miFormulario,"Estudiantes": Estudiantes})
    else:
        miFormulario = formSetEstudiante(initial={'nombre':estudiante.nombre,'apellido':estudiante.apellido,'email':estudiante.email})

        return render(request,"AppCoder/editarEstudiante.html",{"miFormulario":miFormulario,"nombre":nombre_estudiante})

def loginWeb(request): 
    if request.method == "POST":
        user = authenticate(username = request.POST['user'],password = request.POST['password'])
        if user is not None:
            login(request, user)
            return render(request,"Appcoder/inicio.html")
        else:
            return render(request,'Appcoder/login.html',{'error':'usuario o contraseña incorrectos'})
    else:
        return render(request,'Appcoder/login.html')    
    
def registro(request):
    if request.method == "POST":
        userCreate = UserCreationForm(request.POST)
        if userCreate is not None:  
            userCreate.save()
            return render(request, "Appcoder/login.html")
        
    else:

        return render(request, "Appcoder/registro.html")
@login_required    
def perfilview (request):

    return render(request, 'Appcoder/Perfil/Perfil.html')
@login_required  
def editarPerfil(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance = usuario)
        if form.is_valid():
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            return render(request,'Appcoder/Perfil/Perfil.html')
    else:
        form = UserEditForm(initial = {'username': usuario.username, 'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name}) 
        return render(request,'Appcoder/Perfil/editarPerfil.html',{"form": form})  
    
@login_required 
def changePassword(request):
        usuario = request.user
        if request.method == "POST":
            form = ChangePasswordForm(data = request.POST, user = usuario )
            if form.is_valid():
                if request.POST['new_password1'] == request.POST['new_password2']:
                 user = form.save()
                 update_session_auth_hash(request, user)
                return HttpResponse("Las contraseñas no coinciden") 

            return render(request,"Appcoder/inicio.html")
        else:
            form = ChangePasswordForm(user = usuario)
            return render (request, "Appcoder\Perfil\changePassword.html", {"form": form})    
        
@login_required 
def editAvatar(request):
    form = AvatarForm(request,POST, request.FILES)
    print(form)
    print(form.is_valid())
    if form.is_valid():
        user = User.objects.get(username = request.user)
        avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id = request.user.id)
        avatar.save()
        avatar = Avatar.objects.filter(user = request.user.id)
        try:
            avatar = avatar[0].image.url
        except:
            avatar = None
        return render(request,"Appcoder/inicio.html",{'avatar': avatar}) 
    else:
        try:
            avatar = avatar.objects.filter(user = request.user.id)
            form = AvatarForm()
        except:
            form = AvatarForm()
    return render(request,'Appcoder/Avatar.html',{'form': form})            

def getavatar():
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return avatar        