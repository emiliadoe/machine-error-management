from django.contrib import admin
from .models import Machine, ErrorCode, ErrorProtocol

# Register your models here.

admin.site.register(Machine)

admin.site.register(ErrorCode)

admin.site.register(ErrorProtocol)