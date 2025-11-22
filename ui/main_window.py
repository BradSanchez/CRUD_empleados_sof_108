import customtkinter as ctk
from tkinter import messagebox
from ui.sidebar import Sidebar
from ui.data_table import DataTable
from ui.dialogs import ConfigDialog, ConfirmDialog, show_success, show_error
from ui.forms import *
from config.ui_config import ICONS

class MainWindow(ctk.CTk):
    """Ventana principal de la aplicación"""
    
    def __init__(self, db_connection, crud_ops):
        super().__init__()
        
        self.db = db_connection
        self.crud = crud_ops
        self.current_table = None
        
        # Configuración de ventana
        self.title("CRUD SOF108 - Gestión de Empleados")
        self.geometry("1400x800")
        
        # Tema moderno
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Layout principal
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Crear componentes
        self.create_sidebar()
        self.create_main_area()
        
        # Seleccionar primera tabla por defecto
        self.sidebar.select_table("empleados")
    
    def create_sidebar(self):
        """Crea la barra lateral"""
        self.sidebar = Sidebar(
            self,
            on_table_select=self.load_table,
            on_config=self.show_config
        )
        self.sidebar.grid(row=0, column=0, sticky="nsew")
    
    def create_main_area(self):
        """Crea el área principal"""
        # Frame principal
        self.main_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        
        # Barra superior
        self.create_topbar()
        
        # Área de contenido (tabla)
        self.content_frame = ctk.CTkFrame(self.main_frame, corner_radius=0)
        self.content_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.content_frame.grid_rowconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(0, weight=1)
    
    def create_topbar(self):
        """Crea la barra superior con título y botones"""
        topbar = ctk.CTkFrame(self.main_frame, height=80, corner_radius=0)
        topbar.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 0))
        topbar.grid_columnconfigure(0, weight=1)
        
        # Título
        self.title_label = ctk.CTkLabel(topbar, text="👥 Empleados", 
                                       font=("Segoe UI", 24, "bold"))
        self.title_label.grid(row=0, column=0, sticky="w", padx=20, pady=10)
        
        # Frame de botones
        button_frame = ctk.CTkFrame(topbar, fg_color="transparent")
        button_frame.grid(row=0, column=1, sticky="e", padx=20, pady=10)
        
        # Botones de acción
        self.add_btn = ctk.CTkButton(
            button_frame,
            text=f"{ICONS['add']} Agregar",
            command=self.add_record,
            height=35,
            width=120,
            fg_color="#10b981",
            hover_color="#059669"
        )
        self.add_btn.pack(side="left", padx=5)
        
        self.edit_btn = ctk.CTkButton(
            button_frame,
            text=f"{ICONS['edit']} Editar",
            command=self.edit_record,
            height=35,
            width=120
        )
        self.edit_btn.pack(side="left", padx=5)
        
        self.delete_btn = ctk.CTkButton(
            button_frame,
            text=f"{ICONS['delete']} Eliminar",
            command=self.delete_record,
            height=35,
            width=120,
            fg_color="#ef4444",
            hover_color="#dc2626"
        )
        self.delete_btn.pack(side="left", padx=5)
        
        self.refresh_btn = ctk.CTkButton(
            button_frame,
            text=f"{ICONS['refresh']} Actualizar",
            command=self.refresh_data,
            height=35,
            width=120,
            fg_color="#6b7280",
            hover_color="#4b5563"
        )
        self.refresh_btn.pack(side="left", padx=5)
    
    def load_table(self, table_name):
        """Carga los datos de una tabla"""
        self.current_table = table_name
        
        # Actualizar título
        table_titles = {
            "regiones": "📊 Regiones",
            "paises": "🌍 Países",
            "locaciones": "📍 Locaciones",
            "departamentos": "🏢 Departamentos",
            "puestos": "💼 Puestos",
            "empleados": "👥 Empleados",
            "historico": "📜 Histórico"
        }
        self.title_label.configure(text=table_titles.get(table_name, table_name))
        
        # Deshabilitar botón editar para histórico
        if table_name == "historico":
            self.edit_btn.configure(state="disabled")
            self.delete_btn.configure(state="disabled")
        else:
            self.edit_btn.configure(state="normal")
            self.delete_btn.configure(state="normal")
        
        # Cargar datos
        self.refresh_data()
    
    def refresh_data(self):
        """Actualiza los datos de la tabla actual"""
        if not self.current_table:
            return
        
        # Obtener datos según la tabla
        table_methods = {
            "regiones": self.crud.get_regiones,
            "paises": self.crud.get_paises,
            "locaciones": self.crud.get_locaciones,
            "departamentos": self.crud.get_departamentos,
            "puestos": self.crud.get_puestos,
            "empleados": self.crud.get_empleados,
            "historico": self.crud.get_historico
        }
        
        method = table_methods.get(self.current_table)
        if method:
            success, columns, data = method()
            
            if success:
                # Limpiar frame de contenido
                for widget in self.content_frame.winfo_children():
                    widget.destroy()
                
                # Crear nueva tabla
                self.data_table = DataTable(self.content_frame, columns)
                self.data_table.grid(row=0, column=0, sticky="nsew")
                self.data_table.load_data(data)
            else:
                show_error(f"Error al cargar datos: {columns}")
    
    def add_record(self):
        """Abre formulario para agregar registro"""
        forms = {
            "regiones": RegionForm,
            "paises": PaisForm,
            "locaciones": LocacionForm,
            "departamentos": DepartamentoForm,
            "puestos": PuestoForm,
            "empleados": EmpleadoForm,
            "historico": HistoricoForm
        }
        
        form_class = forms.get(self.current_table)
        if form_class:
            form_class(self, self.crud, self.refresh_data)
    
    def edit_record(self):
        """Abre formulario para editar registro"""
        if not hasattr(self, 'data_table'):
            return
        
        selected = self.data_table.get_selected_row()
        if not selected:
            show_error("Seleccione un registro para editar")
            return
        
        forms = {
            "regiones": RegionForm,
            "paises": PaisForm,
            "locaciones": LocacionForm,
            "departamentos": DepartamentoForm,
            "puestos": PuestoForm,
            "empleados": EmpleadoForm
        }
        
        form_class = forms.get(self.current_table)
        if form_class:
            form_class(self, self.crud, self.refresh_data, edit_data=selected)
    
    def delete_record(self):
        """Elimina un registro"""
        if not hasattr(self, 'data_table'):
            return
        
        selected = self.data_table.get_selected_row()
        if not selected:
            show_error("Seleccione un registro para eliminar")
            return
        
        # Obtener ID del registro (primera columna)
        record_id = selected[0]
        
        def confirm_delete():
            delete_methods = {
                "regiones": self.crud.delete_region,
                "paises": self.crud.delete_pais,
                "locaciones": self.crud.delete_locacion,
                "departamentos": self.crud.delete_departamento,
                "puestos": self.crud.delete_puesto,
                "empleados": self.crud.delete_empleado
            }
            
            method = delete_methods.get(self.current_table)
            if method:
                success, msg = method(record_id)
                
                if success:
                    show_success("Registro eliminado correctamente")
                    self.refresh_data()
                else:
                    show_error(msg)
        
        ConfirmDialog(
            self,
            "Confirmar Eliminación",
            f"¿Está seguro de eliminar este registro?\n\nEsta acción no se puede deshacer.",
            confirm_delete
        )
    
    def show_config(self):
        """Muestra diálogo de configuración"""
        ConfigDialog(self, self.db, lambda: None)
