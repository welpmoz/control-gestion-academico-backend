from django.contrib import admin
from .models import Docente, DistribucionCargaAcademica, Carrera, Curso

# Register your models here.
admin.site.register(Docente)
admin.site.register(DistribucionCargaAcademica)
admin.site.register(Curso)
admin.site.register(Carrera)