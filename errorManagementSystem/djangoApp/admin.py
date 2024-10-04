from django.contrib import admin
from .models import Machine, ErrorCode

# Register your models here.

admin.site.register(Machine)

admin.site.register(ErrorCode)