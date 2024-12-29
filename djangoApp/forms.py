from django import forms
from .models import Machine, ErrorCode, ErrorProtocol
from cloudinary.forms import CloudinaryFileField
from django.contrib.auth.forms import AuthenticationForm


class MachineForm(forms.ModelForm):
    documents = CloudinaryFileField(
        options={
            'resource_type': 'raw',
            'folder': 'machine_documents'
        },
        required= False
    )
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
        fields = [ 'error_code', 'category', 'notes']

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Benutzername'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Passwort'})
