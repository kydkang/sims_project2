from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Description(models.Model):  
    DEPT_CHOICES=(
        ('AR', 'Análisis de Riesgos'), 
        ('AH', 'Asistencia Humanitaria'), 
        ('CGAJ', 'Cordinación General de Asesoría Jurídica'), 
        ('EIRD', 'Estratégia Internacionales para la Reducción de Riesgos' ), 
        ('FDCGR', 'Fortalecimiento y Desarrollo de capacidades en Gestión de Riesgos' ), 
        ('GI', 'Gestión de la Información'), 
        ('GR', 'Gestión de Riesgos'), 
        ('MEA', 'Monitoreo de Eventos Adversos'), 
        ('OP', 'Operaciones'), 
        ('PEGR', 'Política y Estandares de Gestión de Riesgos'), 
    )

    SEQ_CHOICES=(
        ('101', '101'), ('102', '102'), ('103', '103'), ('104', '104'), ('105', '105'),
        ('106', '106'), ('107', '107'), ('108', '108'), ('109', '109'), ('110', '110'),
    )

    sequence = models.CharField(max_length=3, choices=SEQ_CHOICES) 
    department = models.CharField(max_length=5, choices=DEPT_CHOICES)
    index_name = models.CharField(max_length=50)
    description = models.TextField() 

    def __str__(self):
        return self.department 
        