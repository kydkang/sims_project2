from django.db import models
from django.urls import reverse

class Index102(models.Model):  
    department = "SNGRE DEPARTMENT Two 222"
    index_name = "Index 222 name is Percentage of Damage"
    description = "Here 222 is the description of the index ....... "

    data_one = models.IntegerField()
    data_two = models.DecimalField(max_digits=5, decimal_places=2)
    data_three = models.DecimalField(max_digits=5, decimal_places=2)
    calculated_value = models.CharField(max_length=32, blank=True, )  # to make it not visible in admin, use  editable=False

    def calculate(self):
        return self.data_one + self.data_two

    def save(self, *args, **kwargs):
        self.calculated_value =  self.calculate() 
        super(Index102, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.data_one) + "   " + str(self.data_two)

    def get_absolute_url(self):
        # or  return reverse('index_detail', args=[str(self.id)])
        return reverse('sims102:index_detail', kwargs={'pk': str(self.id)})

