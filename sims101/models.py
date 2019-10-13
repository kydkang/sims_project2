from django.db import models
from django.urls import reverse

class Index101(models.Model):  
    department = "SNGRE DEPARTMENT ONE"
    index_name = "Index name is oneOneOne"
    description = "Here is the description of the index one....... "
    
    data_one = models.IntegerField()
    data_two = models.DecimalField(max_digits=5, decimal_places=2)
    calculated_value = models.CharField(max_length=32, blank=True, )  # to make it not visible in admin, use  editable=False

    class Meta:
        permissions = [
            ("index_manager", "Index Manager"), 
        ]

    def calculate(self):
        return self.data_one + self.data_two

    def save(self, *args, **kwargs):
        self.calculated_value =  self.calculate() 
        super(Index101, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.data_one) + "   " + str(self.data_two)

    def get_absolute_url(self):
        # or  return reverse('index_detail', args=[str(self.id)])
        return reverse('sims101:index_detail', kwargs={'pk': str(self.id)})
        # or you need to add success_url in CreateView and UpdateView

