# import os
# import sys
# import traceback

# # 1. Tu ruta absoluta
# ruta_proyecto = '/home/cencosto/python/django/ks-control-panel'
# sys.path.insert(0, ruta_proyecto)

# # 2. Tu carpeta de configuración
# os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

# try:
#     # Intentamos arrancar Django
#     from django.core.wsgi import get_wsgi_application
#     application = get_wsgi_application()
    
# except Exception as e:
#     # Si Django explota, capturamos el error y lo mostramos en la web
#     def application(environ, start_response):
#         status = '500 Internal Server Error'
#         headers = [('Content-Type', 'text/plain; charset=utf-8')]
#         start_response(status, headers)
        
#         error_trace = traceback.format_exc()
#         mensaje = f"🚨 ERROR AL INICIAR DJANGO 🚨\n\nPor favor, copia este texto y envíaselo a tu asistente:\n\n{error_trace}"
#         return [mensaje.encode('utf-8')]


import os
import sys

# 1. Agrega la ruta actual de forma automática (así evitamos errores de tipeo en las carpetas)
cwd = os.path.dirname(__file__)
sys.path.insert(0, cwd)

# 2. Apunta a la carpeta interna de tu proyecto (la que tiene los guiones bajos y el archivo settings.py)
# NOTA: Cambia 'ks_control_panel' si el nombre de la carpeta interna es distinto
os.environ['DJANGO_SETTINGS_MODULE'] = 'ks_control_panel.settings'

# 3. Arranca Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()