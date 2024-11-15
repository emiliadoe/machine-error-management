from .models import ErrorProtocol
from django.utils.translation import get_language

def global_data(request):
    protocols = ErrorProtocol.objects.all().order_by('-timestamp')
    language = get_language()
    return {
        'protocols': protocols,
        'LANGUAGE_CODE': language
    }