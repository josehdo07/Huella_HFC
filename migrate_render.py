# migrate_render.py
import os
import django

# Configura la variable de entorno para apuntar a tus settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "miapp.settings")

# Inicializa Django
django.setup()

# Ejecuta las migraciones
from django.core.management import call_command
call_command("migrate")

print("Migraciones ejecutadas correctamente ✅")
