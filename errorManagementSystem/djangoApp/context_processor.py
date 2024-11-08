from .models import ErrorProtocol

def global_data(request):
    protocols = ErrorProtocol.objects.all().order_by('-timestamp')
    return {
        'protocols': protocols
    }