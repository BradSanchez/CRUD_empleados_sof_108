import customtkinter as ctk
from config.ui_config import ICONS

class Sidebar(ctk.CTkFrame):
    """Barra lateral de navegación"""
    
    def __init__(self, parent, on_table_select, on_config):
        super().__init__(parent, width=250, corner_radius=0)
        
        self.on_table_select = on_table_select
        self.on_config = on_config
        
        self.selected_button = None
        self.buttons = {}
        
        self.create_widgets()
    
    def create_widgets(self):
        # Logo/Título
        title_frame = ctk.CTkFrame(self, fg_color="transparent")
        title_frame.pack(fill="x", padx=15, pady=20)
        
        ctk.CTkLabel(title_frame, text="CRUD SOF108", 
                    font=("Segoe UI", 20, "bold")).pack()
        ctk.CTkLabel(title_frame, text="Gestión de Empleados", 
                    font=("Segoe UI", 11), text_color="gray").pack()
        
        # Separador
        separator = ctk.CTkFrame(self, height=2, fg_color="gray30")
        separator.pack(fill="x", padx=15, pady=10)
        
        # Menú de tablas
        ctk.CTkLabel(self, text="TABLAS", font=("Segoe UI", 10, "bold"), 
                    text_color="gray").pack(anchor="w", padx=15, pady=(10, 5))
        
        tables = [
            ("regiones", "Regiones"),
            ("paises", "Países"),
            ("locaciones", "Locaciones"),
            ("departamentos", "Departamentos"),
            ("puestos", "Puestos"),
            ("empleados", "Empleados"),
            ("historico", "Histórico")
        ]
        
        for table_id, table_name in tables:
            icon = ICONS.get(table_id, "📄")
            btn = ctk.CTkButton(
                self,
                text=f"{icon}  {table_name}",
                command=lambda t=table_id: self.select_table(t),
                anchor="w",
                height=40,
                fg_color="transparent",
                hover_color=("gray70", "gray30"),
                font=("Segoe UI", 13)
            )
            btn.pack(fill="x", padx=10, pady=2)
            self.buttons[table_id] = btn
        
        # Espaciador
        ctk.CTkFrame(self, fg_color="transparent").pack(fill="both", expand=True)
        
        # Separador inferior
        separator2 = ctk.CTkFrame(self, height=2, fg_color="gray30")
        separator2.pack(fill="x", padx=15, pady=10)
        
        # Botones de configuración
        config_btn = ctk.CTkButton(
            self,
            text=f"{ICONS['config']}  Configuración",
            command=self.on_config,
            anchor="w",
            height=40,
            fg_color="transparent",
            hover_color=("gray70", "gray30"),
            font=("Segoe UI", 12)
        )
        config_btn.pack(fill="x", padx=10, pady=(2, 15))
    
    def select_table(self, table_id):
        """Selecciona una tabla y actualiza el estilo"""
        # Resetear botón anterior
        if self.selected_button:
            self.selected_button.configure(fg_color="transparent")
        
        # Seleccionar nuevo botón
        btn = self.buttons[table_id]
        btn.configure(fg_color=("gray75", "gray25"))
        self.selected_button = btn
        
        # Llamar callback
        self.on_table_select(table_id)
