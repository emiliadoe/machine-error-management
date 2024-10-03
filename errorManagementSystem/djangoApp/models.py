from django.db import models

# Create your models here.


class Machine(models.Model):

    class Meta:
        verbose_name = 'Machine'
        verbose_name_plural = 'Machines'

    name = models.CharField(max_length=50)

    description = models.CharField(max_length=400)

    def __str__(self):
        return self.name

