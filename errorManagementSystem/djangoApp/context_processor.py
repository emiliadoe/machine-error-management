from .models import ErrorProtocol

def global_data(request):
    
    protocols = ErrorProtocol.objects.all()  


    return {
        'protocols': protocols
    }