from django import forms
from .models import Machine, ErrorCode


class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['name', 'description','notes', 'documents','image']

class ErrorCodeForm(forms.ModelForm):
    class Meta:
        model = ErrorCode
        fields = ['machine', 'error_code', 'error_description','solution', 'images', 'files']

