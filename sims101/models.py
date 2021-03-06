from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from commons.models import Description
from django.shortcuts import get_object_or_404

class Index101(models.Model):       
    SEQUENCE = '101'
    description = models.ForeignKey(Description, on_delete=models.CASCADE) 
    data_one = models.IntegerField(_('FT'), )
    data_two = models.IntegerField(_('DT'), )
    data_three = models.IntegerField(_('PT'), )
    calculated_value = models.DecimalField(_('NPFD'), max_digits=7, decimal_places=2, blank=True, )
 
    class Meta:
        permissions = [
            ("index101_contributor", "index101_contributor"), 
            ("index101_validator",   "index101_validator"), 
        ]
        ordering = ['id'] 

    def calculate(self):         ##  also need to change  ajax_calculate() function 
        return ((self.data_one + self.data_two) / self.data_three ) * 100000

    def save(self, *args, **kwargs):
        self.calculated_value =  self.calculate() 
        # self.description = Description.objects.get(sequence=self.SEQUENCE)
        self.description = get_object_or_404(Description, sequence=self.SEQUENCE)
        super(Index101, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.data_one) + ",    " + str(self.data_two)

    # def get_absolute_url(self):
    #     # or  return reverse('sims101:index_detail', args=[str(self.id)])
    #     return reverse('sims101:index_detail', kwargs={'pk': str(self.id)})



