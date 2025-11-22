import customtkinter as ctk
from tkinter import messagebox

class ConfigDialog(ctk.CTkToplevel):
    """Diálogo de configuración de conexión a base de datos"""
    
    def __init__(self, parent, db_connection, on_success):
        super().__init__(parent)
        
        self.db_connection = db_connection
        self.on_success = on_success
        
        self.title("Configuración de Conexión")
        self.geometry("500x400")
        self.resizable(False, False)
        
        # Centrar ventana
        self.transient(parent)
        self.grab_set()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Frame principal
        main_frame = ctk.CTkFrame(self, corner_radius=0)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Título
        title = ctk.CTkLabel(main_frame, text="⚙️ Configuración de Base de Datos", 
                            font=("Segoe UI", 18, "bold"))
        title.pack(pady=(0, 20))
        
        # Servidor
        ctk.CTkLabel(main_frame, text="Servidor *", font=("Segoe UI", 12)).pack(anchor="w", pady=(10, 5))
        self.server_entry = ctk.CTkEntry(main_frame, placeholder_text="localhost o IP del servidor", height=35)
        self.server_entry.pack(fill="x", pady=(0, 10))
        
        # Tipo de autenticación
        ctk.CTkLabel(main_frame, text="Tipo de Autenticación *", font=("Segoe UI", 12)).pack(anchor="w", pady=(10, 5))
        self.auth_var = ctk.StringVar(value="Windows")
        auth_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        auth_frame.pack(fill="x", pady=(0, 10))
        
        ctk.CTkRadioButton(auth_frame, text="Windows", variable=self.auth_var, 
                          value="Windows", command=self.toggle_auth).pack(side="left", padx=(0, 20))
        ctk.CTkRadioButton(auth_frame, text="SQL Server", variable=self.auth_var, 
                          value="SQL", command=self.toggle_auth).pack(side="left")
        
        # Usuario
        ctk.CTkLabel(main_frame, text="Usuario", font=("Segoe UI", 12)).pack(anchor="w", pady=(10, 5))
        self.username_entry = ctk.CTkEntry(main_frame, placeholder_text="Usuario de SQL Server", height=35)
        self.username_entry.pack(fill="x", pady=(0, 10))
        self.username_entry.configure(state="disabled")
        
        # Contraseña
        ctk.CTkLabel(main_frame, text="Contraseña", font=("Segoe UI", 12)).pack(anchor="w", pady=(10, 5))
        self.password_entry = ctk.CTkEntry(main_frame, placeholder_text="Contraseña", show="*", height=35)
        self.password_entry.pack(fill="x", pady=(0, 20))
        self.password_entry.configure(state="disabled")
        
        # Botones
        button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        button_frame.pack(fill="x", pady=(10, 0))
        
        self.test_btn = ctk.CTkButton(button_frame, text="🔍 Probar Conexión", 
                                      command=self.test_connection, height=35)
        self.test_btn.pack(side="left", expand=True, fill="x", padx=(0, 5))
        
        self.save_btn = ctk.CTkButton(button_frame, text="💾 Guardar y Conectar", 
                                      command=self.save_and_connect, height=35, 
                                      fg_color="#10b981", hover_color="#059669")
        self.save_btn.pack(side="left", expand=True, fill="x", padx=(5, 0))
    
    def toggle_auth(self):
        """Habilita/deshabilita campos según tipo de autenticación"""
        if self.auth_var.get() == "Windows":
            self.username_entry.configure(state="disabled")
            self.password_entry.configure(state="disabled")
        else:
            self.username_entry.configure(state="normal")
            self.password_entry.configure(state="normal")
    
    def test_connection(self):
        """Prueba la conexión sin guardar"""
        server = self.server_entry.get().strip()
        if not server:
            messagebox.showerror("Error", "Ingrese el nombre del servidor")
            return
        
        auth_type = self.auth_var.get()
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        
        if auth_type == "SQL" and (not username or not password):
            messagebox.showerror("Error", "Ingrese usuario y contraseña para autenticación SQL Server")
            return
        
        self.test_btn.configure(state="disabled", text="Probando...")
        self.update()
        
        success, message = self.db_connection.test_connection(server, auth_type, username, password)
        
        self.test_btn.configure(state="normal", text="🔍 Probar Conexión")
        
        if success:
            messagebox.showinfo("Éxito", "✅ " + message)
        else:
            messagebox.showerror("Error de Conexión", message)
    
    def save_and_connect(self):
        """Guarda configuración y conecta"""
        server = self.server_entry.get().strip()
        if not server:
            messagebox.showerror("Error", "Ingrese el nombre del servidor")
            return
        
        auth_type = self.auth_var.get()
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        
        if auth_type == "SQL" and (not username or not password):
            messagebox.showerror("Error", "Ingrese usuario y contraseña para autenticación SQL Server")
            return
        
        self.save_btn.configure(state="disabled", text="Conectando...")
        self.update()
        
        success, message = self.db_connection.test_connection(server, auth_type, username, password)
        
        if success:
            from config.database_config import DatabaseConfig
            DatabaseConfig.save_config(server, auth_type, username, password)
            messagebox.showinfo("Éxito", "✅ Configuración guardada y conexión establecida")
            self.on_success()
            self.destroy()
        else:
            self.save_btn.configure(state="normal", text="💾 Guardar y Conectar")
            messagebox.showerror("Error de Conexión", message)


class ConfirmDialog(ctk.CTkToplevel):
    """Diálogo de confirmación elegante"""
    
    def __init__(self, parent, title, message, on_confirm):
        super().__init__(parent)
        
        self.on_confirm = on_confirm
        self.result = False
        
        self.title(title)
        self.geometry("400x200")
        self.resizable(False, False)
        
        self.transient(parent)
        self.grab_set()
        
        # Frame principal
        main_frame = ctk.CTkFrame(self, corner_radius=0)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Mensaje
        msg_label = ctk.CTkLabel(main_frame, text=message, font=("Segoe UI", 14), 
                                wraplength=350, justify="center")
        msg_label.pack(pady=30)
        
        # Botones
        button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        button_frame.pack(fill="x", pady=(10, 0))
        
        cancel_btn = ctk.CTkButton(button_frame, text="Cancelar", 
                                   command=self.cancel, height=35,
                                   fg_color="#6b7280", hover_color="#4b5563")
        cancel_btn.pack(side="left", expand=True, fill="x", padx=(0, 5))
        
        confirm_btn = ctk.CTkButton(button_frame, text="Confirmar", 
                                    command=self.confirm, height=35,
                                    fg_color="#ef4444", hover_color="#dc2626")
        confirm_btn.pack(side="left", expand=True, fill="x", padx=(5, 0))
    
    def confirm(self):
        self.result = True
        self.on_confirm()
        self.destroy()
    
    def cancel(self):
        self.result = False
        self.destroy()


def show_success(message):
    """Muestra mensaje de éxito"""
    messagebox.showinfo("Éxito", f"✅ {message}")

def show_error(message):
    """Muestra mensaje de error"""
    messagebox.showerror("Error", f"❌ {message}")

def show_warning(message):
    """Muestra mensaje de advertencia"""
    messagebox.showwarning("Advertencia", f"⚠️ {message}")
