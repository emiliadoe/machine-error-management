from django import forms
from .models import Machine, ErrorCode, ErrorProtocol


class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['name', 'description','notes', 'documents','image']

class ErrorCodeForm(forms.ModelForm):
    class Meta:
        model = ErrorCode
        fields = ['machine', 'error_code', 'error_description','solution', 'images', 'files']

class ErrorProtocolForm(forms.ModelForm):
    class Meta:
        model = ErrorProtocol
        fields = [ 'error_code', 'notes']

