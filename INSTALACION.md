# 📦 Guía de Instalación Detallada - CRUD SOF108

Esta guía proporciona instrucciones paso a paso para instalar y configurar la aplicación CRUD SOF108.

## 🔍 Verificación de Requisitos

### 1. Verificar Python

Abrir CMD o PowerShell y ejecutar:

```bash
python --version
```

Debe mostrar Python 3.8 o superior. Si no está instalado:

1. Descargar desde: https://www.python.org/downloads/
2. Durante la instalación, **MARCAR** la opción "Add Python to PATH"
3. Reiniciar la terminal después de instalar

### 2. Verificar SQL Server

1. Abrir **SQL Server Management Studio (SSMS)**
2. Conectarse al servidor
3. Verificar que la base de datos **SOF108** existe
4. Anotar el nombre del servidor (aparece en la barra de título de SSMS)

Ejemplos de nombres de servidor:
- `localhost`
- `.\SQLEXPRESS`
- `DESKTOP-ABC123\SQLEXPRESS`
- `192.168.1.100`

### 3. Verificar ODBC Driver

**Método 1: Interfaz Gráfica**
1. Presionar `Win + R`
2. Escribir `odbcad32` y presionar Enter
3. Ir a la pestaña "Drivers"
4. Buscar "ODBC Driver 17 for SQL Server"

**Método 2: PowerShell**
```powershell
Get-OdbcDriver | Where-Object {$_.Name -like "*SQL Server*"}
```

Si no aparece ningún driver, continuar con la instalación.

## 🚀 Instalación Paso a Paso

### Paso 1: Instalar ODBC Driver (si no está instalado)

1. Descargar ODBC Driver 17 for SQL Server:
   - https://docs.microsoft.com/sql/connect/odbc/download-odbc-driver-for-sql-server

2. Ejecutar el instalador descargado

3. Seguir el asistente de instalación (Next → Next → Install)

4. Reiniciar la computadora (recomendado)

### Paso 2: Preparar el Proyecto

1. Descargar o clonar el proyecto en una carpeta, por ejemplo:
   ```
   C:\Users\TuUsuario\CRUD_empleados_sof_108
   ```

2. Abrir CMD o PowerShell en esa carpeta:
   - **Método 1**: Shift + Click derecho en la carpeta → "Abrir ventana de PowerShell aquí"
   - **Método 2**: Abrir CMD y navegar con `cd`:
     ```bash
     cd C:\Users\TuUsuario\CRUD_empleados_sof_108
     ```

### Paso 3: Crear Entorno Virtual (Opcional pero Recomendado)

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows CMD:
venv\Scripts\activate.bat

# En Windows PowerShell:
venv\Scripts\Activate.ps1

# En Git Bash:
source venv/Scripts/activate
```

Si PowerShell da error de permisos, ejecutar como Administrador:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Paso 4: Instalar Dependencias

```bash
pip install -r requirements.txt
```

**Si hay errores**, intentar instalar una por una:

```bash
pip install pyodbc
pip install customtkinter
pip install Pillow
pip install tkcalendar
```

**Problemas comunes:**

- **Error con pyodbc en Windows**: Descargar wheel desde https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyodbc
  ```bash
  pip install pyodbc-4.0.XX-cpXX-cpXX-win_amd64.whl
  ```

- **Error con Pillow**: Actualizar pip primero
  ```bash
  python -m pip install --upgrade pip
  pip install Pillow
  ```

### Paso 5: Verificar Instalación

```bash
python -c "import pyodbc; import customtkinter; print('✅ Todo instalado correctamente')"
```

Si no hay errores, la instalación fue exitosa.

## ⚙️ Configuración Inicial

### Paso 1: Preparar Información de Conexión

Antes de ejecutar la aplicación, tener a mano:

1. **Nombre del Servidor SQL Server**
   - Verificar en SSMS (barra de título al conectarse)
   - Ejemplos: `localhost`, `.\SQLEXPRESS`, `MIPC\SQLEXPRESS`

2. **Tipo de Autenticación**
   - **Windows Authentication** (recomendado): No requiere usuario/contraseña
   - **SQL Server Authentication**: Requiere usuario y contraseña

3. **Credenciales** (solo si usas SQL Server Authentication)
   - Usuario: `sa` o el usuario que creaste
   - Contraseña: La contraseña del usuario

### Paso 2: Ejecutar la Aplicación

```bash
python main.py
```

### Paso 3: Configurar Conexión

1. Se abrirá automáticamente la ventana de configuración

2. Completar los campos:

   **Servidor:**
   ```
   localhost          # Si SQL Server está en tu PC
   .\SQLEXPRESS       # Si usas SQL Server Express
   192.168.1.100      # Si está en otra PC de la red
   ```

   **Tipo de Autenticación:**
   - Seleccionar "Windows" o "SQL Server"

   **Usuario y Contraseña:**
   - Solo completar si seleccionaste "SQL Server"

3. Hacer clic en **"🔍 Probar Conexión"**

4. Si aparece "✅ Conexión exitosa", hacer clic en **"💾 Guardar y Conectar"**

## 🔧 Solución de Problemas de Instalación

### Error: "python no se reconoce como comando"

**Causa**: Python no está en el PATH del sistema

**Solución**:
1. Reinstalar Python marcando "Add Python to PATH"
2. O agregar manualmente:
   - Buscar la carpeta de instalación de Python (ej: `C:\Python39`)
   - Agregar al PATH del sistema

### Error: "pip no se reconoce como comando"

**Solución**:
```bash
python -m pip install --upgrade pip
```

Luego usar `python -m pip` en lugar de solo `pip`:
```bash
python -m pip install -r requirements.txt
```

### Error: "Microsoft Visual C++ 14.0 is required"

**Causa**: Falta el compilador de C++ para instalar pyodbc

**Solución**:
1. Descargar e instalar "Microsoft C++ Build Tools":
   - https://visualstudio.microsoft.com/visual-cpp-build-tools/
2. Durante la instalación, seleccionar "Desktop development with C++"
3. Reiniciar e intentar instalar pyodbc nuevamente

### Error: "ODBC Driver not found" al ejecutar

**Solución**:
1. Verificar que ODBC Driver 17 está instalado (ver Paso 1)
2. Si no está, instalarlo desde el enlace oficial
3. Si persiste, la aplicación intentará usar el driver "SQL Server" genérico

### Error: "Access Denied" al activar entorno virtual en PowerShell

**Solución**:
```powershell
# Ejecutar PowerShell como Administrador
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Error de conexión: "Login failed"

**Verificar**:
1. Usuario y contraseña correctos
2. El usuario tiene permisos en la base de datos SOF108
3. SQL Server permite el tipo de autenticación seleccionado

**Habilitar autenticación mixta en SQL Server**:
1. Abrir SSMS
2. Click derecho en el servidor → Properties
3. Security → SQL Server and Windows Authentication mode
4. Reiniciar el servicio de SQL Server

### Error: "Cannot open database SOF108"

**Verificar**:
1. La base de datos SOF108 existe
2. El usuario tiene acceso a esa base de datos

**Dar permisos**:
```sql
USE SOF108;
GRANT SELECT, INSERT, UPDATE, DELETE TO [tu_usuario];
```

## 📋 Checklist de Instalación

Marcar cada paso completado:

- [ ] Python 3.8+ instalado y en PATH
- [ ] SQL Server instalado y ejecutándose
- [ ] Base de datos SOF108 creada
- [ ] ODBC Driver 17 instalado
- [ ] Proyecto descargado/clonado
- [ ] Entorno virtual creado (opcional)
- [ ] Dependencias instaladas (`pip install -r requirements.txt`)
- [ ] Verificación exitosa (`python -c "import pyodbc; import customtkinter"`)
- [ ] Información de conexión preparada
- [ ] Aplicación ejecutada (`python main.py`)
- [ ] Conexión configurada y probada

## 🎉 ¡Instalación Completa!

Si todos los pasos se completaron exitosamente, la aplicación debería estar funcionando.

Para ejecutar la aplicación en el futuro:

```bash
# Navegar a la carpeta del proyecto
cd C:\Users\TuUsuario\CRUD_empleados_sof_108

# Activar entorno virtual (si lo usas)
venv\Scripts\activate

# Ejecutar aplicación
python main.py
```

## 📞 Ayuda Adicional

Si sigues teniendo problemas:

1. Revisar el archivo `README.md` para más información
2. Verificar que SQL Server está ejecutándose (Services.msc)
3. Probar la conexión directamente en SSMS con las mismas credenciales
4. Revisar los logs de error de SQL Server

---

**¿Todo funcionando?** ¡Excelente! Ahora puedes empezar a usar la aplicación. 🚀
