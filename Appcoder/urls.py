from django.urls import path
from django.contrib.auth.views import LogoutView
from Appcoder.views import  inicio, cursos,acercaDeMi, estudiantes, profesores, setEstudiantes,getEstudiantes,buscarEstudiante,setCursos,getCursos,buscarCursos,setProfesores,getProfesores,buscarProfesores,eliminarEstudiante,editarEstudiante,loginWeb,registro,perfilview,editarPerfil,changePassword,editAvatar,createPost,verPosts,eliminarPost,enviarMensaje,bandejaEntrada,verMensajes

urlpatterns = [
    

    
    path('inicio/', inicio, name="Inicio"),
    path('cursos/', cursos,name="Cursos"),
    path('acercaDeMi/', acercaDeMi,name="acercaDeMi"),
    path('estudiantes/', estudiantes,name="Estudiantes"),
    path('profesores/', profesores,name="Profesores"),
    path('setEstudiantes/', setEstudiantes,name="setEstudiantes"),
    path('getEstudiantes/', getEstudiantes,name="getEstudiantes"),
    path('buscarEstudiante/', buscarEstudiante,name="buscarEstudiante"),
    path('setCursos/', setCursos,name="setCursos"),
    path('getCursos/', getCursos,name="getCursos"),
    path('buscarCursos/', buscarCursos,name="buscarCursos"),
    path('setProfesores/', setProfesores,name="setProfesores"),
    path('getProfesores/', getProfesores,name="getProfesores"),
    path('buscarProfesores/', buscarProfesores,name="buscarProfesores"),
    path('eliminarEstudiante/<nombre_estudiante>', eliminarEstudiante,name="eliminarEstudiante"),
    path('editarEstudiante/<nombre_estudiante>', editarEstudiante,name="editarEstudiante"),
    path('login/',loginWeb, name="login"),
    path('registro/',registro, name="registro"),
    path('Logout/',LogoutView.as_view(template_name = "Appcoder/login.html"), name="logout"),
    path('perfil/',perfilview, name="perfil"),
    path('Perfil/editarPerfil/',editarPerfil, name="editarPerfil"),
    path('Perfil/changePassword/',changePassword, name="changePassword"),
    path('Perfil/changeAvatar/',editAvatar, name="editAvatar"),
    path('create_post/', createPost, name='create_post'),
    path('ver_posts/', verPosts, name='ver_posts'),
    path('eliminar_post/<int:pk>/', eliminarPost, name='eliminar_post'),
    path('enviarMensaje/', enviarMensaje, name='enviarMensaje'),
    path('bandejaEntrada/', bandejaEntrada, name='bandejaEntrada'),
    path('verMensajes/<int:mensaje_id>/', verMensajes, name='verMensajes'),
    
    
    
    
    
    
]
