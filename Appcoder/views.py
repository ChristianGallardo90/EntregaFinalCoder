from django.shortcuts import render,redirect
from django.http import HttpResponse
from Appcoder.models import Estudiante,Curso,Profesor,Avatar
from Appcoder.forms import formSetEstudiante,formSetCursos,formSetProfesor,UserEditForm,ChangePasswordForm,AvatarForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator
from .models import Mensaje
from django.contrib.auth import logout
from datetime import date



# Create your views here.


@login_required
def inicio(request):
     avatar = getavatar(request)
     return render(request,"AppCoder/inicio.html",{"avatar": avatar})
@login_required
def cursos(request):
    avatar = getavatar(request)
    return render(request,"AppCoder/cursos.html",{"avatar": avatar})
@login_required

def profesores(request):
    avatar = getavatar(request)
    return render(request,"AppCoder/profesores.html",{"avatar": avatar})

@login_required
def estudiantes(request):
    avatar = getavatar(request)
    return render(request,"AppCoder/estudiantes.html",{"avatar": avatar})

@login_required
def acercaDeMi(request):
    avatar = getavatar(request)
    return render(request,"AppCoder/acercaDeMi.html",{"avatar": avatar})

@login_required
def setEstudiantes(request):
    avatar = getavatar(request)
    Estudiantes = Estudiante.objects.all()
       
    if request.method == 'POST':
        miFormulario = formSetEstudiante(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            estudiantes = Estudiante(nombre=data["nombre"],apellido=data["apellido"],email=data["email"])
            estudiantes.save()
            miFormulario = formSetEstudiante()
            return render(request,"AppCoder/setEstudiantes.html",{"miFormulario":miFormulario,"Estudiantes": Estudiantes,"avatar": avatar})

    else:
        miFormulario = formSetEstudiante
    return render(request,"AppCoder/setEstudiantes.html",{"miFormulario":miFormulario,"Estudiantes": Estudiantes,"avatar": avatar})

@login_required
def getEstudiantes(request):
    avatar = getavatar(request)
    return render(request,"AppCoder/getEstudiantes.html",{"avatar": avatar})

@login_required
def buscarEstudiante(request):
    avatar = getavatar(request)
    if request.GET["nombre"]:
         nombre = request.GET["nombre"]
         estudiantes = Estudiante.objects.filter(nombre = nombre)
         return render(request,"AppCoder/getEstudiantes.html",{"estudiantes":estudiantes,"avatar": avatar})
    else:
        respuesta = "no se enviaron datos"
    return HttpResponse(respuesta)

@login_required
def setCursos(request):
    avatar = getavatar(request)
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
    return render(request,"AppCoder/setCursos.html",{"miFormulario":miFormulario,"avatar": avatar})
      
@login_required   
def getCursos(request):
    avatar = getavatar(request)
    return render(request,"AppCoder/getCursos.html",{"avatar": avatar})
   
@login_required
def buscarCursos(request):
    avatar = getavatar(request)
    if request.GET["nombre"]:
         nombre = request.GET["nombre"]
         cursos = Curso.objects.filter(nombre = nombre)
         return render(request,"AppCoder/getCursos.html",{"cursos":cursos,"avatar": avatar})
    else:
        respuesta = "no se enviaron datos"
    return HttpResponse(respuesta) 
    
@login_required
def setProfesores(request):
    avatar = getavatar(request)
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
    return render(request,"AppCoder/setProfesores.html",{"miFormulario":miFormulario,"avatar": avatar})  

@login_required
def getProfesores(request):
    avatar = getavatar(request)
    return render(request,"AppCoder/getProfesores.html",{"avatar": avatar})  

@login_required
def buscarProfesores(request):
    avatar = getavatar(request)
    if request.GET["nombre"]:
         nombre = request.GET["nombre"]
         profesores = Profesor.objects.filter(nombre = nombre)
         return render(request,"AppCoder/getProfesores.html",{"profesores":profesores,"avatar": avatar})
    else:
        respuesta = "no se enviaron datos"
    return HttpResponse(respuesta)     

@login_required  
def leerEstudiantes(request):
    avatar = getavatar(request)
    Estudiantes = Estudiante.objects.all()
    return render (request, "Appcoder/setEstudiantes.html",{"Estudiantes":Estudiantes,"avatar": avatar})

from django.contrib.auth.decorators import login_required

@login_required
def eliminarEstudiante(request, nombre_estudiante):
    avatar = getavatar(request)
    
    if request.user.is_superuser:
        estudiante = Estudiante.objects.get(nombre=nombre_estudiante)
        estudiante.delete()
        miFormulario = formSetEstudiante()
        Estudiantes = Estudiante.objects.all()
        return render(request, "Appcoder/setEstudiantes.html", {"miFormulario": miFormulario, "Estudiantes": Estudiantes, "avatar": avatar})
    else:
        return HttpResponse("No tienes permisos para eliminar este estudiante.")

from django.contrib.auth.decorators import login_required

@login_required
def editarEstudiante(request, nombre_estudiante):
    avatar = getavatar(request)
    
    if request.user.is_superuser:
        estudiante = Estudiante.objects.get(nombre=nombre_estudiante)
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
                return render(request, "AppCoder/setEstudiantes.html", {"miFormulario": miFormulario, "Estudiantes": Estudiantes})
        else:
            miFormulario = formSetEstudiante(initial={'nombre': estudiante.nombre, 'apellido': estudiante.apellido, 'email': estudiante.email})
            return render(request, "AppCoder/editarEstudiante.html", {"miFormulario": miFormulario, "nombre": nombre_estudiante, "avatar": avatar})
    else:
        return HttpResponse("No tienes permisos para editar este estudiante.")


def loginWeb(request): 
    avatar = getavatar(request)
    if request.method == "POST":
        user = authenticate(username = request.POST['user'],password = request.POST['password'])
        if user is not None:
            login(request, user)
            return render(request,"Appcoder/inicio.html")
        else:
            return render(request,'Appcoder/login.html',{'error':'usuario o contraseña incorrectos',"avatar": avatar})
    else:
        return render(request,'Appcoder/login.html',{"avatar": avatar})    
    
def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirigir al usuario a la página de inicio de sesión
    else:
        form = UserCreationForm()

    return render(request, "Appcoder/registro.html", {'form': form})
    
@login_required    
def perfilview (request):
    avatar = getavatar(request)

    return render(request, 'Appcoder/Perfil/Perfil.html',{"avatar": avatar})

@login_required  
def editarPerfil(request):
    avatar = getavatar(request)
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
            return render(request,'Appcoder/Perfil/Perfil.html',{"avatar": avatar})
    else:
        form = UserEditForm(initial = {'username': usuario.username, 'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name}) 
        return render(request,'Appcoder/Perfil/editarPerfil.html',{"form": form,"avatar": avatar})  
    
@login_required 
def changePassword(request):
        avatar = getavatar(request)
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
            return render (request, "Appcoder\Perfil\changePassword.html", {"form": form,"avatar": avatar})    
        
@login_required 
def editAvatar(request):
    form = AvatarForm(request.POST, request.FILES)
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
    return render(request,'Appcoder/Perfil/avatar.html',{'form': form})  
          
@login_required 
def getavatar(request):

    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return avatar        

@login_required 
def createPost(request):
    avatar = getavatar(request)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  
            post.subtitle = form.cleaned_data['subtitle']  
            post.author_name = form.cleaned_data['author_name'] 
            post.fecha_creacion = date.today()
            post.save()  
            
            return redirect('ver_posts',)
    else:
        form = PostForm()
    
    return render(request, 'Appcoder/createPost.html', {'form': form,"avatar": avatar})

@login_required 
def verPosts(request):
    avatar = getavatar(request)
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 3)  

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'Appcoder/verPosts.html', {'posts': posts, 'avatar': avatar})

@login_required
def eliminarPost(request, pk):
    if request.user.is_superuser:
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('ver_posts')
    else:
        return HttpResponse("No tienes permisos para eliminar este post.")

@login_required
def bandejaEntrada(request):
    avatar = getavatar(request)
    mensajes = Mensaje.objects.filter(destinatario=request.user).order_by('-fecha_creacion')
    return render(request, 'Appcoder/bandejaEntrada.html', {'mensajes': mensajes,"avatar": avatar})

@login_required
def enviarMensaje(request):
    avatar = getavatar(request)
    if request.method == 'POST':
        destinatario_id = request.POST.get('destinatario')
        contenido = request.POST.get('contenido')
        destinatario = User.objects.get(id=destinatario_id)
        mensaje = Mensaje(remitente=request.user, destinatario=destinatario, contenido=contenido)
        mensaje.save()
        return redirect('bandejaEntrada')
    else:
        usuarios = User.objects.exclude(id=request.user.id)
        return render(request, 'Appcoder/enviarMensajes.html', {'usuarios': usuarios,"avatar": avatar})

@login_required
def verMensajes(request, mensaje_id=None):
    avatar = getavatar(request)
    if request.method == 'POST':
        # Lógica para procesar la acción de la solicitud POST
        pass
    else:
        mensaje = Mensaje.objects.get(id=mensaje_id)
        if mensaje.destinatario == request.user:
            return render(request, 'Appcoder/verMensajes.html', {'mensaje': mensaje,"avatar": avatar})
        else:
            return redirect('bandejaEntrada')
        
def logout_view(request):


    
    logout(request)
    return redirect('inicio.html',)       






