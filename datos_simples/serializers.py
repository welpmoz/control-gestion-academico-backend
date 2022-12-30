from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Docente, Curso, DistribucionCargaAcademica, Carrera

class DocenteSerializer(HyperlinkedModelSerializer):
  class Meta:
    model = Docente
    fields = ['nombre', 'staff', 'admin']

class CursoSerializer(HyperlinkedModelSerializer):
  class Meta:
    model = Curso
    fields = ['nombre']

class CarreraSerializer(HyperlinkedModelSerializer):
  class Meta:
    model = Carrera
    fields = ['nombre']

class DistribucionCargaAcademicaSerializer(HyperlinkedModelSerializer):
  class Meta:
    model = DistribucionCargaAcademica
    fields = ['archivo']