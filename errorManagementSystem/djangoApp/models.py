from django.db import models

# Create your models here.


class Machine(models.Model):

    class Meta:
        verbose_name = 'Machine'
        verbose_name_plural = 'Machines'

    name = models.CharField(max_length=50)

    description = models.CharField(max_length=400)

    notes = models.CharField(max_length=200, blank=True)

    documents = models.FileField(upload_to="files", blank=True, null=True)

    def __str__(self):
        return self.name
    
class ErrorCode(models.Model):

    class Meta: 
        verbose_name = 'ErrorCode'
        verbose_name_plural = 'ErrorCodes'

    error_code = models.CharField(max_length=20)

    error_description = models.CharField(max_length=400)

    solution = models.CharField(max_length=400)

    machine = models.ForeignKey(Machine, on_delete=models.CASCADE) 

