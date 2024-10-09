from django import forms
from .models import Machine, ErrorCode

class SearchForm(forms.ModelForm):

    title = forms.CharField(required=False)
    description = forms.CharField(required=False)

    class Meta:
        model = Machine
        fields = ['name', 'description']


class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['name', 'description','notes', 'documents']

class ErrorCodeForm(forms.ModelForm):
    class Meta:
        model = ErrorCode
        fields = ['error_code', 'error_description','solution', 'machine']
