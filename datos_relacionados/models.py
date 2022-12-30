from django.db import models
from datos_simples.models import Curso, Carrera, Docente

# Create your models here.
class CursoActivo(models.Model):
  codigo = models.CharField(max_length=10)
  datos_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
  datos_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

  def __str__(self) -> str:
    return f"{self.datos_curso} - {self.datos_carrera}"

class Horario(models.Model):
  curso_activo = models.ForeignKey(CursoActivo, on_delete=models.CASCADE)
  creditos = models.IntegerField()
  tipo = models.CharField(max_length=1)
  grupo = models.CharField(max_length=1)
  ht = models.TimeField()
  hp = models.TimeField()
  dia = models.CharField(max_length=15)
  hi = models.TimeField()
  hf = models.TimeField()
  aula = models.CharField(max_length=20)
  docente = models.ForeignKey(Docente, on_delete=models.CASCADE)