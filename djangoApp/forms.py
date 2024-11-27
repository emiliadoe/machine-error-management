from django import forms
from .models import Machine, ErrorCode, ErrorProtocol
from cloudinary.forms import CloudinaryFileField
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm


MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB


class MachineForm(forms.ModelForm):
    documents = CloudinaryFileField(
        options={
            'resource_type': 'raw',
            'folder': 'machine_documents'
        }
    )
    class Meta:
        model = Machine
        fields = ['name', 'description','notes', 'documents','image']

    def clean_documents(self):
        document = self.cleaned_data.get('documents')
        if document:
            if not document.url.endswith('.pdf'):
                raise ValidationError('Die Datei muss im PDF-Format vorliegen.')
            if document.size > MAX_FILE_SIZE:
                raise ValidationError('Die Datei ist zu groß.')

        return document

class ErrorCodeForm(forms.ModelForm):
    class Meta:
        model = ErrorCode
        fields = ['machine', 'error_code', 'error_description','solution', 'images', 'files']

class ErrorProtocolForm(forms.ModelForm):
    class Meta:
        model = ErrorProtocol
        fields = [ 'error_code', 'notes']

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Benutzername'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Passwort'})


class LogFilterForm(forms.Form):
    machine = forms.ModelChoiceField(
        queryset=Machine.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'filter-dropdown'})
    )
    code = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'filter-dropdown'})
    )
    date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'filter-dropdown'})
    )
