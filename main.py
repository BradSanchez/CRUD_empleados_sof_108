"""
CRUD SOF108 - Sistema de Gestión de Empleados
Aplicación con interfaz gráfica moderna para gestionar base de datos SQL Server
"""

import customtkinter as ctk
from tkinter import messagebox
import sys

from config.database_config import DatabaseConfig
from database.connection import DatabaseConnection
from database.crud_operations import CRUDOperations
from ui.main_window import MainWindow
from ui.dialogs import ConfigDialog

def main():
    """Función principal de la aplicación"""
    
    # Crear conexión a base de datos
    db_connection = DatabaseConnection()
    
    # Verificar si existe configuración
    if not DatabaseConfig.config_exists():
        # Primera vez - mostrar configuración
        root = ctk.CTk()
        root.withdraw()  # Ocultar ventana principal
        
        def on_config_success():
            root.quit()
        
        config_dialog = ConfigDialog(root, db_connection, on_config_success)
        root.mainloop()
        
        # Si no se configuró, salir
        if not DatabaseConfig.config_exists():
            sys.exit(0)
    
    # Conectar a la base de datos
    success, message = db_connection.connect()
    
    if not success:
        root = ctk.CTk()
        root.withdraw()
        messagebox.showerror("Error de Conexión", 
                           f"No se pudo conectar a la base de datos:\n\n{message}\n\n"
                           "Verifique la configuración y vuelva a intentar.")
        
        def on_config_success():
            root.quit()
        
        config_dialog = ConfigDialog(root, db_connection, on_config_success)
        root.mainloop()
        
        # Intentar conectar nuevamente
        success, message = db_connection.connect()
        if not success:
            messagebox.showerror("Error", "No se pudo establecer conexión. La aplicación se cerrará.")
            sys.exit(1)
    
    # Crear operaciones CRUD
    crud_ops = CRUDOperations(db_connection)
    
    # Crear y ejecutar ventana principal
    app = MainWindow(db_connection, crud_ops)
    
    # Manejar cierre de ventana
    def on_closing():
        if messagebox.askokcancel("Salir", "¿Desea cerrar la aplicación?"):
            db_connection.close()
            app.destroy()
    
    app.protocol("WM_DELETE_WINDOW", on_closing)
    app.mainloop()

if __name__ == "__main__":
    main()
