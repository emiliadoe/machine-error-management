from django.db import models
from django.utils import timezone


class Machine(models.Model):

    class Meta:
        verbose_name = 'Machine'
        verbose_name_plural = 'Machines'

    name = models.CharField(max_length=50)

    description = models.CharField(max_length=400)

    notes = models.CharField(max_length=200, blank=True)

    documents = models.FileField(upload_to="files", blank=True, null=True)

    image = models.ImageField(upload_to="machine_image", blank=True, null=True)

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

    images = models.ImageField(upload_to="error-pictures", blank=True, null=True)
    
    files = models.FileField(upload_to="error-files", blank=True, null=True)

    def __str__(self):
        return self.error_code 



class ErrorProtocol(models.Model):

    class Meta:
        verbose_name = 'Error'

    timestamp = models.DateTimeField(default=timezone.now)  
    
    error_code = models.ForeignKey('ErrorCode', on_delete=models.CASCADE, related_name='error_protocols') 
    
    notes = models.TextField(blank=True, null=True) 
    
    machine = models.ForeignKey('Machine', on_delete=models.SET_NULL, null=True, blank=True) 
    
    def save(self, *args, **kwargs):
        if not self.machine: 
            self.machine = self.error_code.machine  
        
        super(ErrorProtocol, self).save(*args, **kwargs) 

    def __str__(self):
        return f"ErrorProtocol {self.id} - {self.timestamp}"

