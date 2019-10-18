from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Description(models.Model):  
    DEPT_CHOICES=(
        ('dept_one', 'Direccion ONE'), 
        ('dept_two', 'Direccion TWO'), 
    )

    SEQ_CHOICES=(
        ('101', '101'), 
        ('102', '102'), 
    )

    sequence = models.CharField(max_length=3, choices=SEQ_CHOICES) 
    department = models.CharField(max_length=30, choices=DEPT_CHOICES)
    index_name = models.CharField(max_length=50)
    description = models.TextField() 

    def __str__(self):
        return self.department 
        