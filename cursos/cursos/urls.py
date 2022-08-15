"""cursos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import listar_cursos,curso_cadastrar,editar_curso,remover_curso

urlpatterns = [
    path('curso/', listar_cursos, name='listar_cursos'),
    path('curso_cadastrar/',curso_cadastrar, name='curso_cadastrar'),
    path('curso_editar/<int:id>/',editar_curso, name='editar_curso'),
    path('curso_remover/<int:id>/',remover_curso, name='remover_curso'),
    path('admin/', admin.site.urls),
]
