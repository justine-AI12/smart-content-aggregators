import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aggregator_core.aggregator_core.settings')
django.setup()

from djongo import connection

def check_connection():
    conn = connection.get_connection()
    try:
        conn.server_info()  # Test de connexion
        print("✅ Connexion MongoDB active")
        print(f"Bases disponibles: {conn.list_database_names()}")
    except Exception as e:
        print(f"❌ Erreur de connexion: {e}")

if __name__ == '__main__':
    check_connection()