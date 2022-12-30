from rest_framework.serializers import HyperlinkedModelSerializer
from datos_simples.serializers import CursoSerializer, CarreraSerializer
from .models import Horario, CursoActivo
from datos_simples.serializers import DocenteSerializer

class CursoActivoSerializer(HyperlinkedModelSerializer):
  class Meta:
    model = CursoActivo
    fields = ['codigo', 'datos_curso', 'datos_carrera']

  def to_representation(self, instance):
    rep = super().to_representation(instance)
    rep['datos_curso'] = CursoSerializer(instance.datos_curso).data
    rep['datos_carrera'] = CarreraSerializer(instance.datos_carrera).data
    return rep

class HorarioSerializer(HyperlinkedModelSerializer):
  class Meta:
    model = Horario
    fields = ['curso_activo', 'creditos', 'tipo', 'grupo',
      'ht', 'hp', 'dia', 'hi', 'hf', 'aula', 'docente']

  def to_representation(self, instance):
    rep = super().to_representation(instance)
    #rep['curso_activo'] = CursoActivoSerializer(instance.curso_activo).data
    rep['docente'] = DocenteSerializer(instance.docente).data
    return rep