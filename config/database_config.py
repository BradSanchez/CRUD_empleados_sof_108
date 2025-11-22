import json
import os

class DatabaseConfig:
    """Gestiona la configuración de conexión a SQL Server"""
    
    CONFIG_FILE = "db_config.json"
    
    @staticmethod
    def save_config(server, auth_type, username="", password=""):
        """Guarda la configuración de conexión"""
        config = {
            "server": server,
            "auth_type": auth_type,
            "username": username,
            "password": password,
            "database": "SOF108"
        }
        with open(DatabaseConfig.CONFIG_FILE, 'w') as f:
            json.dump(config, f)
    
    @staticmethod
    def load_config():
        """Carga la configuración guardada"""
        if os.path.exists(DatabaseConfig.CONFIG_FILE):
            with open(DatabaseConfig.CONFIG_FILE, 'r') as f:
                return json.load(f)
        return None
    
    @staticmethod
    def config_exists():
        """Verifica si existe configuración guardada"""
        return os.path.exists(DatabaseConfig.CONFIG_FILE)
