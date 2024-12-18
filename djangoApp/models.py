from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField


class Machine(models.Model):
    class Meta:
        verbose_name = 'Machine'
        verbose_name_plural = 'Machines'
        ordering = ['name']
    name = models.CharField(max_length=50, db_index=True)
    description = models.CharField(max_length=400, db_index=True)
    notes = models.CharField(max_length=200, blank=True, db_index=True)
    documents = CloudinaryField('documents', blank=True, null=True, folder="machine_documents")
    image = CloudinaryField('image', blank=True, null=True, folder="machine_images")

    def secure_url(self):
        return self.documents.url.replace('http://', 'https://')

    def __str__(self):
        return self.name

    
class ErrorCode(models.Model):
    class Meta: 
        verbose_name = 'ErrorCode'
        verbose_name_plural = 'ErrorCodes'
        ordering = ['error_code']
    error_code = models.CharField(max_length=20)
    error_description = models.CharField(max_length=400)
    solution = models.CharField(max_length=400)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE) 
    images = CloudinaryField('image', blank=True, null=True, folder="error_images")
    files = CloudinaryField('documents', blank=True, null=True, folder="error_files")

    def __str__(self):
        return self.error_code 



class ErrorProtocol(models.Model):
    class Meta:
        verbose_name = 'Error'
        ordering = ['-timestamp']

    TYPE = [
        ('Fehler', 'Fehler'),
        ('Störung', 'Störung'),
        ('Ausfall', 'Ausfall'), 
        ('Schaden', 'Schaden'),
    ]

    timestamp = models.DateTimeField(default=timezone.now)  
    error_code = models.ForeignKey('ErrorCode', on_delete=models.CASCADE, related_name='error_protocols') 
    notes = models.TextField(blank=True, null=True) 
    machine = models.ForeignKey('Machine', on_delete=models.SET_NULL, null=True, blank=True) 
    category = models.CharField(
        blank=True,
        choices=TYPE,
        max_length=15,
        default='Fehler'
          )
    
    def save(self, *args, **kwargs):
        if not self.machine and self.error_code:
            self.machine = self.error_code.machine  
        super(ErrorProtocol, self).save(*args, **kwargs) 

    def __str__(self):
        return f"Error Eintrag {self.id} - {self.timestamp}"

