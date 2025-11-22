# 🚀 Inicio Rápido - CRUD SOF108

Guía rápida para poner en marcha la aplicación en 5 minutos.

## ✅ Pre-requisitos

- ✔️ Python 3.8+ instalado
- ✔️ SQL Server ejecutándose
- ✔️ Base de datos SOF108 creada

## 📦 Instalación Rápida

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Ejecutar aplicación

```bash
python main.py
```

### 3. Configurar conexión

En la ventana que aparece:

- **Servidor**: `localhost` o `.\SQLEXPRESS`
- **Autenticación**: Seleccionar "Windows"
- Click en "Probar Conexión"
- Click en "Guardar y Conectar"

## 🎯 Uso Básico

### Agregar un empleado

1. Click en "👥 Empleados" en el menú lateral
2. Click en "➕ Agregar"
3. Completar formulario
4. Click en "💾 Guardar"

### Editar un empleado

1. Seleccionar fila en la tabla
2. Click en "✏️ Editar"
3. Modificar datos
4. Click en "💾 Guardar"

### Eliminar un empleado

1. Seleccionar fila en la tabla
2. Click en "🗑️ Eliminar"
3. Confirmar

### Buscar

- Escribir en el campo de búsqueda sobre la tabla
- Los resultados se filtran automáticamente

## 🔧 Problemas Comunes

### "No module named 'pyodbc'"
```bash
pip install pyodbc
```

### "ODBC Driver not found"
Descargar e instalar: https://docs.microsoft.com/sql/connect/odbc/download-odbc-driver-for-sql-server

### "Cannot connect to server"
- Verificar que SQL Server está ejecutándose
- Verificar el nombre del servidor en SSMS

## 📚 Más Información

- Ver `README.md` para documentación completa
- Ver `INSTALACION.md` para guía detallada de instalación
- Ver `database_schema.sql` para crear la base de datos

## 🎨 Características

- ✨ Interfaz moderna con tema claro/oscuro
- 🔍 Búsqueda en tiempo real
- ✅ Validaciones automáticas
- 💾 Configuración persistente
- 🎯 Navegación intuitiva

---

**¿Listo?** ¡Ejecuta `python main.py` y comienza a gestionar tu base de datos! 🚀
