import customtkinter as ctk
from tkinter import ttk

class DataTable(ctk.CTkFrame):
    """Componente de tabla de datos moderna"""
    
    def __init__(self, parent, columns):
        super().__init__(parent, corner_radius=10)
        
        self.columns = columns
        self.data = []
        
        self.create_widgets()
    
    def create_widgets(self):
        # Barra de búsqueda
        search_frame = ctk.CTkFrame(self, fg_color="transparent")
        search_frame.pack(fill="x", padx=10, pady=10)
        
        ctk.CTkLabel(search_frame, text="🔍", font=("Segoe UI", 16)).pack(side="left", padx=(0, 5))
        self.search_entry = ctk.CTkEntry(search_frame, placeholder_text="Buscar...", height=35)
        self.search_entry.pack(side="left", fill="x", expand=True)
        self.search_entry.bind("<KeyRelease>", self.on_search)
        
        # Frame para la tabla con scrollbar
        table_frame = ctk.CTkFrame(self)
        table_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        
        # Scrollbars
        vsb = ttk.Scrollbar(table_frame, orient="vertical")
        hsb = ttk.Scrollbar(table_frame, orient="horizontal")
        
        # Treeview (tabla)
        self.tree = ttk.Treeview(table_frame, columns=self.columns, show="tree headings",
                                 yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        vsb.config(command=self.tree.yview)
        hsb.config(command=self.tree.xview)
        
        # Configurar columnas
        self.tree.column("#0", width=0, stretch=False)
        for col in self.columns:
            self.tree.heading(col, text=col, anchor="w")
            self.tree.column(col, anchor="w", width=120)
        
        # Estilo de la tabla
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                       background="#2d2d2d",
                       foreground="white",
                       fieldbackground="#2d2d2d",
                       borderwidth=0,
                       font=("Segoe UI", 10))
        style.configure("Treeview.Heading",
                       background="#3d3d3d",
                       foreground="white",
                       borderwidth=0,
                       font=("Segoe UI", 11, "bold"))
        style.map("Treeview",
                 background=[("selected", "#3b82f6")])
        
        # Empaquetar
        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")
        
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)
    
    def load_data(self, data):
        """Carga datos en la tabla"""
        self.data = data
        self.refresh_display(data)
    
    def refresh_display(self, data):
        """Actualiza la visualización de la tabla"""
        # Limpiar tabla
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Insertar datos
        for row in data:
            # Convertir None a cadena vacía
            row_values = [str(val) if val is not None else "" for val in row]
            self.tree.insert("", "end", values=row_values)
    
    def on_search(self, event):
        """Filtra datos según búsqueda"""
        search_term = self.search_entry.get().lower()
        
        if not search_term:
            self.refresh_display(self.data)
            return
        
        # Filtrar datos
        filtered_data = []
        for row in self.data:
            row_str = " ".join([str(val).lower() for val in row if val is not None])
            if search_term in row_str:
                filtered_data.append(row)
        
        self.refresh_display(filtered_data)
    
    def get_selected_row(self):
        """Obtiene la fila seleccionada"""
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            return item["values"]
        return None
    
    def clear(self):
        """Limpia la tabla"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.data = []
