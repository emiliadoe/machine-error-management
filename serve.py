import os
from waitress import serve
from errorManagementSystem.wsgi import application  

if __name__ == "__main__":
    host = os.getenv('HOST', '0.0.0.0')  
    port = int(os.getenv('PORT', '8000'))
    serve(application, host=host, port=port)
