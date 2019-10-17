from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Index101(models.Model):  
    department = "SNGRE DEPARTMENT ONE"
    index_name = "Index name is oneOneOne"
    description = "Mauris fringilla enim massa, quisque ante augue habitasse sed donec a. Nec neque est, iaculis erat viverra fringilla tincidunt, mollis porttitor in quis in, in ac curabitur faucibus sem. Orci congue sapien, phasellus ipsum, risus vivamus eleifend vestibulum phasellus suspendisse. Aliquam tempus risus lacinia sed, lacus duis massa massa, lorem natoque nobis urna, sit eget vivamus urna, et aliquam id et non sed. Ultricies taciti varius, vel phasellus dui diam enim. Nam ullam ut libero erat, veritatis leo et ipsum feugiat laoreet, semper vel natoque pellentesque ligula elementum, sed id erat, arcu fusce. Vitae fusce sodales necessitatibus id, aliquam eleifend libero massa volutpat quam. Vel fermentum sed ullamcorper quisque, bibendum pretium, pede mauris risus volutpat leo sed. Sodales facere nunc non. "    

    data_one = models.IntegerField(_('data one'), )
    data_two = models.DecimalField(_('data two'), max_digits=5, decimal_places=2)
    calculated_value = models.CharField(_('calculated value'), max_length=32, blank=True, )  # to make it not visible in admin, use  editable=False

    class Meta:
        permissions = [
            ("index_manager", "Index Manager"), 
        ]
        ordering = ['id'] 

    def calculate(self):
        return self.data_one + self.data_two

    def save(self, *args, **kwargs):
        self.calculated_value =  self.calculate() 
        super(Index101, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.data_one) + "   " + str(self.data_two)

    def get_absolute_url(self):
        # or  return reverse('sims101:index_detail', args=[str(self.id)])
        return reverse('sims101:index_detail', kwargs={'pk': str(self.id)})
        # or you need to add success_url in CreateView and UpdateView

