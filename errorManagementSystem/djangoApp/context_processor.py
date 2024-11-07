from .models import ErrorProtocol

def global_data(request):
    """
    This function returns context data that will be available in every template.
    In this case, it's the list of all machines and error protocols.
    """
    
    protocols = ErrorProtocol.objects.all()  


    return {
        'protocols': protocols
    }