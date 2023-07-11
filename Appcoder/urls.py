from django.urls import path
from django.contrib.auth.views import LogoutView
from Appcoder.views import inicio, cursos, entregables, estudiantes, profesores, setEstudiantes,getEstudiantes,buscarEstudiante,setCursos,getCursos,buscarCursos,setProfesores,getProfesores,buscarProfesores,eliminarEstudiante,editarEstudiante,loginWeb,registro,perfilview,editarPerfil,changePassword,editAvatar,createPost,detailPost
urlpatterns = [
    
    path('inicio/', inicio, name="Inicio"),
    path('cursos/', cursos,name="Cursos"),
    path('entregables/', entregables,name="Entregables"),
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
    path('post/<int:pk>/', detailPost, name='detail_post'),

    
    
    
]
