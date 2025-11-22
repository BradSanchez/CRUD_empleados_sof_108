import customtkinter as ctk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime

class BaseForm(ctk.CTkToplevel):
    """Clase base para formularios"""
    
    def __init__(self, parent, title, width=500, height=600):
        super().__init__(parent)
        
        self.title(title)
        self.geometry(f"{width}x{height}")
        self.resizable(False, False)
        
        self.transient(parent)
        self.grab_set()
        
        # Frame principal con scroll
        self.main_frame = ctk.CTkScrollableFrame(self, corner_radius=0)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        self.entries = {}
    
    def add_field(self, label, key, field_type="entry", required=True, options=None, **kwargs):
        """Agrega un campo al formulario"""
        label_text = f"{label} *" if required else label
        ctk.CTkLabel(self.main_frame, text=label_text, font=("Segoe UI", 12)).pack(anchor="w", pady=(10, 5))
        
        if field_type == "entry":
            widget = ctk.CTkEntry(self.main_frame, height=35, **kwargs)
        elif field_type == "combobox":
            widget = ctk.CTkComboBox(self.main_frame, height=35, values=options or [], **kwargs)
        elif field_type == "date":
            widget = DateEntry(self.main_frame, width=30, background='darkblue',
                             foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
        
        widget.pack(fill="x", pady=(0, 5))
        self.entries[key] = widget
    
    def add_buttons(self, on_save):
        """Agrega botones de guardar y cancelar"""
        button_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        button_frame.pack(fill="x", pady=(20, 0))
        
        cancel_btn = ctk.CTkButton(button_frame, text="Cancelar", command=self.destroy,
                                   height=35, fg_color="#6b7280", hover_color="#4b5563")
        cancel_btn.pack(side="left", expand=True, fill="x", padx=(0, 5))
        
        save_btn = ctk.CTkButton(button_frame, text="💾 Guardar", command=on_save,
                                height=35, fg_color="#10b981", hover_color="#059669")
        save_btn.pack(side="left", expand=True, fill="x", padx=(5, 0))
    
    def get_value(self, key):
        """Obtiene el valor de un campo"""
        widget = self.entries.get(key)
        if widget:
            if isinstance(widget, DateEntry):
                return widget.get_date().strftime('%Y-%m-%d')
            return widget.get()
        return None
    
    def set_value(self, key, value):
        """Establece el valor de un campo"""
        widget = self.entries.get(key)
        if widget:
            if isinstance(widget, ctk.CTkComboBox):
                widget.set(value)
            elif isinstance(widget, DateEntry):
                if value:
                    widget.set_date(datetime.strptime(str(value)[:10], '%Y-%m-%d'))
            else:
                widget.delete(0, "end")
                widget.insert(0, value if value else "")


# ==================== FORMULARIOS ESPECÍFICOS ====================

class RegionForm(BaseForm):
    def __init__(self, parent, crud_ops, on_success, edit_data=None):
        super().__init__(parent, "Editar Región" if edit_data else "Nueva Región", 400, 250)
        
        self.crud_ops = crud_ops
        self.on_success = on_success
        self.edit_data = edit_data
        
        self.add_field("Nombre de la Región", "nombre", placeholder_text="Ej: América del Norte")
        self.add_buttons(self.save)
        
        if edit_data:
            self.set_value("nombre", edit_data[1])
    
    def save(self):
        nombre = self.get_value("nombre").strip()
        if not nombre:
            messagebox.showerror("Error", "El nombre es obligatorio")
            return
        
        if self.edit_data:
            success, msg = self.crud_ops.update_region(self.edit_data[0], nombre)
        else:
            success, msg = self.crud_ops.add_region(nombre)
        
        if success:
            messagebox.showinfo("Éxito", "✅ Región guardada correctamente")
            self.on_success()
            self.destroy()
        else:
            messagebox.showerror("Error", msg)


class PaisForm(BaseForm):
    def __init__(self, parent, crud_ops, on_success, edit_data=None):
        super().__init__(parent, "Editar País" if edit_data else "Nuevo País", 400, 350)
        
        self.crud_ops = crud_ops
        self.on_success = on_success
        self.edit_data = edit_data
        
        # Obtener regiones
        regiones = crud_ops.get_regiones_list()
        region_options = [f"{r[0]} - {r[1]}" for r in regiones]
        
        self.add_field("Código del País (2 letras)", "id_pais", placeholder_text="Ej: US")
        self.add_field("Nombre del País", "nombre", placeholder_text="Ej: Estados Unidos")
        self.add_field("Región", "region", field_type="combobox", options=region_options)
        self.add_buttons(self.save)
        
        if edit_data:
            self.entries["id_pais"].configure(state="disabled")
            self.set_value("id_pais", edit_data[0])
            self.set_value("nombre", edit_data[1])
            self.set_value("region", f"{edit_data[2]} - {edit_data[3]}")
    
    def save(self):
        id_pais = self.get_value("id_pais").strip().upper()
        nombre = self.get_value("nombre").strip()
        region_str = self.get_value("region")
        
        if not id_pais or not nombre or not region_str:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        if len(id_pais) != 2:
            messagebox.showerror("Error", "El código del país debe tener 2 letras")
            return
        
        id_region = int(region_str.split(" - ")[0])
        
        if self.edit_data:
            success, msg = self.crud_ops.update_pais(id_pais, nombre, id_region)
        else:
            success, msg = self.crud_ops.add_pais(id_pais, nombre, id_region)
        
        if success:
            messagebox.showinfo("Éxito", "✅ País guardado correctamente")
            self.on_success()
            self.destroy()
        else:
            messagebox.showerror("Error", msg)


class LocacionForm(BaseForm):
    def __init__(self, parent, crud_ops, on_success, edit_data=None):
        super().__init__(parent, "Editar Locación" if edit_data else "Nueva Locación", 500, 550)
        
        self.crud_ops = crud_ops
        self.on_success = on_success
        self.edit_data = edit_data
        
        paises = crud_ops.get_paises_list()
        pais_options = [f"{p[0]} - {p[1]}" for p in paises]
        
        self.add_field("Dirección", "direccion", placeholder_text="Ej: Calle Principal 123")
        self.add_field("Código Postal", "codigo_postal", placeholder_text="Ej: 12345")
        self.add_field("Ciudad", "ciudad", placeholder_text="Ej: Madrid")
        self.add_field("Provincia/Estado", "provincia", placeholder_text="Ej: Madrid")
        self.add_field("País", "pais", field_type="combobox", options=pais_options)
        self.add_buttons(self.save)
        
        if edit_data:
            self.set_value("direccion", edit_data[1])
            self.set_value("codigo_postal", edit_data[2])
            self.set_value("ciudad", edit_data[3])
            self.set_value("provincia", edit_data[4])
            self.set_value("pais", f"{edit_data[5]} - {edit_data[6]}")
    
    def save(self):
        direccion = self.get_value("direccion").strip()
        codigo_postal = self.get_value("codigo_postal").strip()
        ciudad = self.get_value("ciudad").strip()
        provincia = self.get_value("provincia").strip()
        pais_str = self.get_value("pais")
        
        if not all([direccion, ciudad, pais_str]):
            messagebox.showerror("Error", "Dirección, ciudad y país son obligatorios")
            return
        
        id_pais = pais_str.split(" - ")[0]
        
        if self.edit_data:
            success, msg = self.crud_ops.update_locacion(self.edit_data[0], direccion, 
                                                         codigo_postal, ciudad, provincia, id_pais)
        else:
            success, msg = self.crud_ops.add_locacion(direccion, codigo_postal, 
                                                      ciudad, provincia, id_pais)
        
        if success:
            messagebox.showinfo("Éxito", "✅ Locación guardada correctamente")
            self.on_success()
            self.destroy()
        else:
            messagebox.showerror("Error", msg)


class DepartamentoForm(BaseForm):
    def __init__(self, parent, crud_ops, on_success, edit_data=None):
        super().__init__(parent, "Editar Departamento" if edit_data else "Nuevo Departamento", 500, 400)
        
        self.crud_ops = crud_ops
        self.on_success = on_success
        self.edit_data = edit_data
        
        empleados = crud_ops.get_empleados_list()
        empleado_options = [""] + [f"{e[0]} - {e[1]}" for e in empleados]
        
        locaciones = crud_ops.get_locaciones_list()
        locacion_options = [f"{l[0]} - {l[1]}" for l in locaciones]
        
        self.add_field("Nombre del Departamento", "nombre", placeholder_text="Ej: Recursos Humanos")
        self.add_field("Supervisor", "supervisor", field_type="combobox", 
                      options=empleado_options, required=False)
        self.add_field("Locación", "locacion", field_type="combobox", options=locacion_options)
        self.add_buttons(self.save)
        
        if edit_data:
            self.set_value("nombre", edit_data[1])
            if edit_data[2]:
                self.set_value("supervisor", str(edit_data[2]))
            self.set_value("locacion", f"{edit_data[3]} - {edit_data[4]}")
    
    def save(self):
        nombre = self.get_value("nombre").strip()
        supervisor_str = self.get_value("supervisor")
        locacion_str = self.get_value("locacion")
        
        if not nombre or not locacion_str:
            messagebox.showerror("Error", "Nombre y locación son obligatorios")
            return
        
        id_supervisor = int(supervisor_str.split(" - ")[0]) if supervisor_str and supervisor_str.strip() else None
        id_locacion = int(locacion_str.split(" - ")[0])
        
        if self.edit_data:
            success, msg = self.crud_ops.update_departamento(self.edit_data[0], nombre, 
                                                            id_supervisor, id_locacion)
        else:
            success, msg = self.crud_ops.add_departamento(nombre, id_supervisor, id_locacion)
        
        if success:
            messagebox.showinfo("Éxito", "✅ Departamento guardado correctamente")
            self.on_success()
            self.destroy()
        else:
            messagebox.showerror("Error", msg)


class PuestoForm(BaseForm):
    def __init__(self, parent, crud_ops, on_success, edit_data=None):
        super().__init__(parent, "Editar Puesto" if edit_data else "Nuevo Puesto", 500, 450)
        
        self.crud_ops = crud_ops
        self.on_success = on_success
        self.edit_data = edit_data
        
        self.add_field("Código del Puesto", "id_puesto", placeholder_text="Ej: IT_PROG")
        self.add_field("Título del Puesto", "titulo", placeholder_text="Ej: Programador")
        self.add_field("Salario Mínimo", "salario_min", placeholder_text="Ej: 30000")
        self.add_field("Salario Máximo", "salario_max", placeholder_text="Ej: 60000")
        self.add_buttons(self.save)
        
        if edit_data:
            self.entries["id_puesto"].configure(state="disabled")
            self.set_value("id_puesto", edit_data[0])
            self.set_value("titulo", edit_data[1])
            self.set_value("salario_min", edit_data[2])
            self.set_value("salario_max", edit_data[3])
    
    def save(self):
        id_puesto = self.get_value("id_puesto").strip().upper()
        titulo = self.get_value("titulo").strip()
        salario_min = self.get_value("salario_min").strip()
        salario_max = self.get_value("salario_max").strip()
        
        if not all([id_puesto, titulo, salario_min, salario_max]):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        try:
            salario_min = int(salario_min)
            salario_max = int(salario_max)
            
            if salario_min >= salario_max:
                messagebox.showerror("Error", "El salario mínimo debe ser menor al máximo")
                return
        except ValueError:
            messagebox.showerror("Error", "Los salarios deben ser números enteros")
            return
        
        if self.edit_data:
            success, msg = self.crud_ops.update_puesto(id_puesto, titulo, salario_min, salario_max)
        else:
            success, msg = self.crud_ops.add_puesto(id_puesto, titulo, salario_min, salario_max)
        
        if success:
            messagebox.showinfo("Éxito", "✅ Puesto guardado correctamente")
            self.on_success()
            self.destroy()
        else:
            messagebox.showerror("Error", msg)


class EmpleadoForm(BaseForm):
    def __init__(self, parent, crud_ops, on_success, edit_data=None):
        super().__init__(parent, "Editar Empleado" if edit_data else "Nuevo Empleado", 550, 700)
        
        self.crud_ops = crud_ops
        self.on_success = on_success
        self.edit_data = edit_data
        
        puestos = crud_ops.get_puestos_list()
        puesto_options = [f"{p[0]} - {p[1]}" for p in puestos]
        
        empleados = crud_ops.get_empleados_list()
        empleado_options = [""] + [f"{e[0]} - {e[1]}" for e in empleados]
        
        departamentos = crud_ops.get_departamentos_list()
        depto_options = [""] + [f"{d[0]} - {d[1]}" for d in departamentos]
        
        self.add_field("Nombre", "nombre", placeholder_text="Ej: Juan")
        self.add_field("Apellido", "apellido", placeholder_text="Ej: Pérez")
        self.add_field("Email", "email", placeholder_text="Ej: juan.perez@empresa.com")
        self.add_field("Teléfono", "telefono", placeholder_text="Ej: +34 123 456 789", required=False)
        self.add_field("Fecha de Contrato", "fecha_contrato", field_type="date")
        self.add_field("Puesto", "puesto", field_type="combobox", options=puesto_options)
        self.add_field("Salario", "salario", placeholder_text="Ej: 45000")
        self.add_field("Comisión", "comision", placeholder_text="Ej: 5000", required=False)
        self.add_field("Supervisor", "supervisor", field_type="combobox", 
                      options=empleado_options, required=False)
        self.add_field("Departamento", "departamento", field_type="combobox", 
                      options=depto_options, required=False)
        self.add_buttons(self.save)
        
        if edit_data:
            self.set_value("nombre", edit_data[1])
            self.set_value("apellido", edit_data[2])
            self.set_value("email", edit_data[3])
            self.set_value("telefono", edit_data[4])
            self.set_value("fecha_contrato", edit_data[5])
            self.set_value("puesto", f"{edit_data[6]} - {edit_data[7]}")
            self.set_value("salario", edit_data[8])
            self.set_value("comision", edit_data[9] if edit_data[9] else "")
            if edit_data[10]:
                self.set_value("supervisor", str(edit_data[10]))
            if edit_data[11]:
                self.set_value("departamento", f"{edit_data[11]} - {edit_data[12]}")
    
    def save(self):
        nombre = self.get_value("nombre").strip()
        apellido = self.get_value("apellido").strip()
        email = self.get_value("email").strip()
        telefono = self.get_value("telefono").strip()
        fecha_contrato = self.get_value("fecha_contrato")
        puesto_str = self.get_value("puesto")
        salario = self.get_value("salario").strip()
        comision = self.get_value("comision").strip()
        supervisor_str = self.get_value("supervisor")
        departamento_str = self.get_value("departamento")
        
        if not all([nombre, apellido, email, fecha_contrato, puesto_str, salario]):
            messagebox.showerror("Error", "Los campos marcados con * son obligatorios")
            return
        
        try:
            salario = int(salario)
            comision = int(comision) if comision else None
        except ValueError:
            messagebox.showerror("Error", "Salario y comisión deben ser números")
            return
        
        id_puesto = puesto_str.split(" - ")[0]
        id_supervisor = int(supervisor_str.split(" - ")[0]) if supervisor_str and supervisor_str.strip() else None
        id_departamento = int(departamento_str.split(" - ")[0]) if departamento_str and departamento_str.strip() else None
        
        if self.edit_data:
            success, msg = self.crud_ops.update_empleado(self.edit_data[0], nombre, apellido, 
                                                        email, telefono, fecha_contrato, id_puesto,
                                                        salario, comision, id_supervisor, id_departamento)
        else:
            success, msg = self.crud_ops.add_empleado(nombre, apellido, email, telefono, 
                                                      fecha_contrato, id_puesto, salario, 
                                                      comision, id_supervisor, id_departamento)
        
        if success:
            messagebox.showinfo("Éxito", "✅ Empleado guardado correctamente")
            self.on_success()
            self.destroy()
        else:
            messagebox.showerror("Error", msg)


class HistoricoForm(BaseForm):
    def __init__(self, parent, crud_ops, on_success):
        super().__init__(parent, "Nuevo Registro Histórico", 550, 500)
        
        self.crud_ops = crud_ops
        self.on_success = on_success
        
        empleados = crud_ops.get_empleados_list()
        empleado_options = [f"{e[0]} - {e[1]}" for e in empleados]
        
        puestos = crud_ops.get_puestos_list()
        puesto_options = [f"{p[0]} - {p[1]}" for p in puestos]
        
        departamentos = crud_ops.get_departamentos_list()
        depto_options = [f"{d[0]} - {d[1]}" for d in departamentos]
        
        self.add_field("Empleado", "empleado", field_type="combobox", options=empleado_options)
        self.add_field("Fecha de Inicio", "fecha_inicio", field_type="date")
        self.add_field("Fecha de Fin", "fecha_fin", field_type="date")
        self.add_field("Puesto", "puesto", field_type="combobox", options=puesto_options)
        self.add_field("Departamento", "departamento", field_type="combobox", options=depto_options)
        self.add_buttons(self.save)
    
    def save(self):
        empleado_str = self.get_value("empleado")
        fecha_inicio = self.get_value("fecha_inicio")
        fecha_fin = self.get_value("fecha_fin")
        puesto_str = self.get_value("puesto")
        departamento_str = self.get_value("departamento")
        
        if not all([empleado_str, fecha_inicio, fecha_fin, puesto_str, departamento_str]):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        id_empleado = int(empleado_str.split(" - ")[0])
        id_puesto = puesto_str.split(" - ")[0]
        id_departamento = int(departamento_str.split(" - ")[0])
        
        success, msg = self.crud_ops.add_historico(id_empleado, fecha_inicio, fecha_fin, 
                                                   id_puesto, id_departamento)
        
        if success:
            messagebox.showinfo("Éxito", "✅ Registro histórico guardado correctamente")
            self.on_success()
            self.destroy()
        else:
            messagebox.showerror("Error", msg)
