import pyodbc
from config.database_config import DatabaseConfig

class DatabaseConnection:
    """Gestiona la conexión a SQL Server"""
    
    def __init__(self):
        self.connection = None
        self.config = None
    
    def connect(self, config=None):
        """Establece conexión con SQL Server"""
        if config is None:
            config = DatabaseConfig.load_config()
        
        if config is None:
            raise Exception("No hay configuración de base de datos")
        
        self.config = config
        
        try:
            if config["auth_type"] == "Windows":
                conn_str = (
                    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                    f"SERVER={config['server']};"
                    f"DATABASE={config['database']};"
                    f"Trusted_Connection=yes;"
                )
            else:
                conn_str = (
                    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                    f"SERVER={config['server']};"
                    f"DATABASE={config['database']};"
                    f"UID={config['username']};"
                    f"PWD={config['password']};"
                )
            
            self.connection = pyodbc.connect(conn_str)
            return True, "Conexión exitosa"
        
        except pyodbc.Error as e:
            error_msg = str(e)
            if "ODBC Driver 17" in error_msg:
                # Intentar con driver alternativo
                try:
                    conn_str = conn_str.replace("ODBC Driver 17", "SQL Server")
                    self.connection = pyodbc.connect(conn_str)
                    return True, "Conexión exitosa"
                except:
                    return False, "Error: Instale ODBC Driver 17 for SQL Server"
            return False, f"Error de conexión: {error_msg}"
    
    def test_connection(self, server, auth_type, username="", password=""):
        """Prueba la conexión sin guardar configuración"""
        config = {
            "server": server,
            "auth_type": auth_type,
            "username": username,
            "password": password,
            "database": "SOF108"
        }
        return self.connect(config)
    
    def execute_query(self, query, params=None):
        """Ejecuta una consulta SELECT"""
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            columns = [column[0] for column in cursor.description]
            results = cursor.fetchall()
            cursor.close()
            
            return True, columns, results
        
        except Exception as e:
            return False, str(e), None
    
    def execute_non_query(self, query, params=None):
        """Ejecuta INSERT, UPDATE, DELETE"""
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            self.connection.commit()
            cursor.close()
            return True, "Operación exitosa"
        
        except Exception as e:
            self.connection.rollback()
            return False, f"Error: {str(e)}"
    
    def close(self):
        """Cierra la conexión"""
        if self.connection:
            self.connection.close()
