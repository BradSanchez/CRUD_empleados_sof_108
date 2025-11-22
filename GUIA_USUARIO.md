# 🚀 Guía Rápida para Usuarios - CRUD SOF108

## 📋 Requisitos Previos

Antes de usar la aplicación, asegúrate de tener:

1. ✅ **Python 3.8+** instalado
2. ✅ **SQL Server** ejecutándose en tu PC
3. ✅ **Base de datos SOF108** creada

---

## 🔧 Instalación (Primera Vez)

### Paso 1: Instalar Dependencias

Abre CMD o PowerShell en la carpeta del proyecto y ejecuta:

```bash
pip install -r requirements.txt
```

### Paso 2: Crear la Base de Datos (si no existe)

1. Abre **SQL Server Management Studio (SSMS)**
2. Abre el archivo `database_schema.sql`
3. Presiona **F5** para ejecutarlo
4. Esto creará la base de datos SOF108 con todas las tablas

---

## 🚀 Ejecutar la Aplicación

### Método Fácil: Doble Click

Haz **doble click** en el archivo `ejecutar.bat`

### Método Alternativo: Línea de Comandos

```bash
python main.py
```

---

## 🔌 Configuración de Conexión (Primera Vez)

Cuando ejecutes la aplicación por primera vez, aparecerá una ventana de configuración:

### 1️⃣ Obtener el Nombre de tu Servidor

**Opción A: Desde SSMS**
- Abre SQL Server Management Studio
- El nombre del servidor aparece en la ventana de conexión
- Ejemplos: `MIPC`, `MIPC\SQLEXPRESS`, `localhost`

**Opción B: Nombres Comunes**
- Si tienes SQL Server Express: `.\SQLEXPRESS` o `localhost\SQLEXPRESS`
- Si tienes SQL Server estándar: Tu nombre de PC o `localhost`

### 2️⃣ Completar la Configuración

```
┌─────────────────────────────────────────┐
│  Servidor *                             │
│  ┌───────────────────────────────────┐ │
│  │ TU-PC  o  .\SQLEXPRESS            │ │  ← Escribe el nombre de tu servidor
│  └───────────────────────────────────┘ │
│                                         │
│  Tipo de Autenticación *                │
│  ● Windows    ○ SQL Server              │  ← Selecciona Windows (más fácil)
│                                         │
│  Usuario (dejar vacío si usas Windows)  │
│  Contraseña (dejar vacío si usas Windows)│
│                                         │
│  [ 🔍 Probar Conexión ]                │  ← Click aquí primero
│  [ 💾 Guardar y Conectar ]             │  ← Luego click aquí
└─────────────────────────────────────────┘
```

### 3️⃣ Probar y Guardar

1. Click en **"🔍 Probar Conexión"**
2. Si aparece "✅ Conexión exitosa", click en **"💾 Guardar y Conectar"**
3. ¡Listo! La aplicación se abrirá

---

## 📝 Uso Básico

### Agregar un Registro

1. Selecciona una tabla del menú lateral (ej: Empleados)
2. Click en **"➕ Agregar"**
3. Completa el formulario
4. Click en **"💾 Guardar"**

### Editar un Registro

1. Selecciona una fila en la tabla
2. Click en **"✏️ Editar"**
3. Modifica los datos
4. Click en **"💾 Guardar"**

### Eliminar un Registro

1. Selecciona una fila en la tabla
2. Click en **"🗑️ Eliminar"**
3. Confirma la eliminación

### Buscar

- Escribe en el campo de búsqueda sobre la tabla
- Los resultados se filtran automáticamente

---

## 🆘 Problemas Comunes

### ❌ "Python no está instalado"

**Solución:**
- Descargar Python desde: https://www.python.org/downloads/
- Durante la instalación, marcar "Add Python to PATH"

### ❌ "No module named 'pyodbc'"

**Solución:**
```bash
pip install -r requirements.txt
```

### ❌ "Cannot connect to server"

**Soluciones:**

1. **Verificar que SQL Server está ejecutándose:**
   - Presiona `Win + R`
   - Escribe `services.msc` y Enter
   - Busca "SQL Server" y verifica que está "Running"

2. **Probar diferentes nombres de servidor:**
   - `localhost`
   - `.\SQLEXPRESS`
   - `TU-PC` (tu nombre de PC)
   - `TU-PC\SQLEXPRESS`

3. **Verificar el nombre correcto:**
   - Abre SSMS
   - El nombre correcto aparece en la ventana de conexión

### ❌ "Database SOF108 not found"

**Solución:**
1. Abre SSMS
2. Ejecuta el archivo `database_schema.sql`
3. Esto creará la base de datos

### ❌ "ODBC Driver not found"

**Solución:**
- Descargar e instalar ODBC Driver 17 for SQL Server
- Link: https://docs.microsoft.com/sql/connect/odbc/download-odbc-driver-for-sql-server

---

## 🔄 Reconfigurar Conexión

Si necesitas cambiar la configuración:

1. Click en **"⚙️ Configuración"** en el menú lateral
2. Modifica los datos
3. Prueba y guarda

---

## 🌓 Cambiar Tema

Click en **"🌓 Cambiar Tema"** para alternar entre modo claro y oscuro.

---

## 📞 Ayuda Adicional

Para más información, consulta:
- `README.md` - Documentación completa
- `FAQ.md` - Preguntas frecuentes
- `EJEMPLOS_USO.md` - Ejemplos prácticos

---

## ✅ Checklist de Inicio

- [ ] Python instalado
- [ ] SQL Server ejecutándose
- [ ] Base de datos SOF108 creada
- [ ] Dependencias instaladas (`pip install -r requirements.txt`)
- [ ] Aplicación ejecutada (`ejecutar.bat` o `python main.py`)
- [ ] Conexión configurada
- [ ] ¡Listo para usar!

---

**¿Problemas?** Revisa la sección de Problemas Comunes o consulta `FAQ.md`
