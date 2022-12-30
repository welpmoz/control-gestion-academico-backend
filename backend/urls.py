"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from datos_simples.views import DocenteViewSet, CursoViewSet, CarreraViewSet, DistribucionCargaAcademicaViewSet, view_adocente
from datos_relacionados.views import CursoActivoViewSet, HorarioViewSet, subirCursosActivos, subirHorarios

router_simple = DefaultRouter()
router_simple.register(r'cursos', CursoViewSet)
router_simple.register(r'docentes', DocenteViewSet)
router_simple.register(r'carreras', CarreraViewSet)
router_simple.register(r'distribuciones_academicas', DistribucionCargaAcademicaViewSet)

router_relacionado = DefaultRouter()
router_relacionado.register(r'cursos_activos', CursoActivoViewSet)
router_relacionado.register(r'horarios', HorarioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_datos_simples/', include(router_simple.urls)),
    path('api_datos_relacionados/', include(router_relacionado.urls)),
    path('add_docentes/', view_adocente),
    path('subir_activos/', subirCursosActivos),
    path('subir_horarios/', subirHorarios),
]
