from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from commons.models import Description

class Index101(models.Model):  
    SEQUENCE = '101'
    description = models.ForeignKey(Description, on_delete=models.CASCADE) 
    data_one = models.IntegerField(_('data one'), )
    data_two = models.DecimalField(_('data two'), max_digits=5, decimal_places=2)
    calculated_value = models.CharField(_('calculated value'), max_length=32, blank=True, )
    # to make a field not visible in admin, use  editable=False
 
    class Meta:
        permissions = [
            ("index_manager", "Index Manager"), 
        ]
        ordering = ['id'] 

    def calculate(self):
        return self.data_one + self.data_two

    def save(self, *args, **kwargs):
        self.calculated_value =  self.calculate() 
        self.description = Description.objects.get(sequence=self.SEQUENCE)
        print(self.description) 
        super(Index101, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.data_one) + "   " + str(self.data_two)

    def get_absolute_url(self):
        # or  return reverse('sims101:index_detail', args=[str(self.id)])
        return reverse('sims101:index_detail', kwargs={'pk': str(self.id)})
        # or you need to add success_url in CreateView and UpdateView


