# 🚀 CRUD SOF108 - Sistema de Gestión de Empleados

Aplicación de escritorio con interfaz gráfica moderna y minimalista para gestionar la base de datos SOF108 en SQL Server.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-5.0+-green.svg)
![SQL Server](https://img.shields.io/badge/SQL%20Server-2016+-red.svg)

## 📋 Características

- ✨ **Interfaz moderna y minimalista** con CustomTkinter
- 🎨 **Tema claro/oscuro** intercambiable
- 🔍 **Búsqueda en tiempo real** en todas las tablas
- ✏️ **Operaciones CRUD completas** para 7 tablas
- 🔐 **Autenticación Windows y SQL Server**
- ✅ **Validaciones robustas** de datos
- 🎯 **Navegación intuitiva** con menú lateral
- 💾 **Configuración persistente** de conexión

## 📊 Tablas Gestionadas

1. **Regiones** - Regiones geográficas
2. **Países** - Países por región
3. **Locaciones** - Ubicaciones físicas
4. **Departamentos** - Departamentos de la empresa
5. **Puestos** - Puestos de trabajo
6. **Empleados** - Información de empleados
7. **Histórico** - Historial laboral

## 🛠️ Requisitos Previos

### Software Necesario

1. **Python 3.8 o superior**
   - Descargar desde: https://www.python.org/downloads/
   - Durante la instalación, marcar "Add Python to PATH"

2. **SQL Server** (cualquier versión)
   - SQL Server Express (gratuito): https://www.microsoft.com/sql-server/sql-server-downloads
   - SQL Server Management Studio (SSMS): https://docs.microsoft.com/sql/ssms/download-sql-server-management-studio-ssms

3. **ODBC Driver 17 for SQL Server**
   - Descargar desde: https://docs.microsoft.com/sql/connect/odbc/download-odbc-driver-for-sql-server
   - **IMPORTANTE**: Este driver es necesario para la conexión

### Base de Datos

La base de datos **SOF108** debe estar creada y funcionando en SQL Server Management Studio con las siguientes tablas:

- REGIONES
- PAISES
- LOCACIONES
- DEPARTAMENTOS
- PUESTOS
- EMPLEADOS
- HISTORICO

## 📦 Instalación

### Paso 1: Clonar o Descargar el Proyecto

```bash
# Si tienes git instalado
git clone <url-del-repositorio>
cd CRUD_empleados_sof_108

# O simplemente descarga y extrae el ZIP
```

### Paso 2: Instalar Dependencias de Python

Abrir terminal/CMD en la carpeta del proyecto y ejecutar:

```bash
pip install -r requirements.txt
```

Si hay problemas con pip, intentar:

```bash
python -m pip install -r requirements.txt
```

### Paso 3: Verificar Instalación de ODBC Driver

Para verificar que el driver ODBC está instalado:

**Windows:**
1. Presionar `Win + R`
2. Escribir `odbcad32` y presionar Enter
3. Ir a la pestaña "Drivers"
4. Buscar "ODBC Driver 17 for SQL Server" o "SQL Server"

Si no aparece, descargar e instalar desde el enlace mencionado en requisitos.

## 🚀 Ejecución

### Primera Vez

1. Ejecutar la aplicación:

```bash
python main.py
```

2. Se abrirá automáticamente la ventana de **Configuración de Conexión**

3. Completar los datos:
   - **Servidor**: Nombre del servidor SQL Server
     - Ejemplos: `localhost`, `.\SQLEXPRESS`, `192.168.1.100`, `DESKTOP-ABC123\SQLEXPRESS`
   - **Tipo de Autenticación**: 
     - **Windows**: Usa las credenciales de Windows (recomendado)
     - **SQL Server**: Requiere usuario y contraseña de SQL Server
   - **Usuario/Contraseña**: Solo si se selecciona autenticación SQL Server

4. Hacer clic en **"🔍 Probar Conexión"** para verificar

5. Si la conexión es exitosa, hacer clic en **"💾 Guardar y Conectar"**

### Ejecuciones Posteriores

La aplicación recordará la configuración y se conectará automáticamente.

```bash
python main.py
```

## 🎯 Guía de Uso

### Navegación

- **Menú Lateral Izquierdo**: Seleccionar la tabla a gestionar
- **Barra Superior**: Botones de acción (Agregar, Editar, Eliminar, Actualizar)
- **Área Central**: Tabla de datos con búsqueda

### Operaciones CRUD

#### ➕ Agregar Registro

1. Seleccionar tabla en el menú lateral
2. Hacer clic en **"➕ Agregar"**
3. Completar el formulario
4. Hacer clic en **"💾 Guardar"**

#### ✏️ Editar Registro

1. Seleccionar una fila en la tabla
2. Hacer clic en **"✏️ Editar"**
3. Modificar los campos necesarios
4. Hacer clic en **"💾 Guardar"**

#### 🗑️ Eliminar Registro

1. Seleccionar una fila en la tabla
2. Hacer clic en **"🗑️ Eliminar"**
3. Confirmar la eliminación

#### 🔍 Buscar

- Escribir en el campo de búsqueda en la parte superior de la tabla
- La búsqueda filtra en tiempo real

#### 🔄 Actualizar

- Hacer clic en **"🔄 Actualizar"** para recargar los datos

### Funciones Adicionales

#### ⚙️ Reconfigurar Conexión

1. Hacer clic en **"⚙️ Configuración"** en el menú lateral
2. Modificar los datos de conexión
3. Probar y guardar

#### 🌓 Cambiar Tema

- Hacer clic en **"🌓 Cambiar Tema"** para alternar entre modo claro y oscuro

## 🔧 Solución de Problemas

### Error: "No module named 'pyodbc'"

**Solución:**
```bash
pip install pyodbc
```

### Error: "ODBC Driver 17 for SQL Server not found"

**Solución:**
1. Descargar e instalar ODBC Driver 17 desde: https://docs.microsoft.com/sql/connect/odbc/download-odbc-driver-for-sql-server
2. Si persiste, la aplicación intentará usar el driver "SQL Server" genérico

### Error: "Login failed for user"

**Causas posibles:**
- Usuario o contraseña incorrectos (autenticación SQL Server)
- El usuario no tiene permisos en la base de datos SOF108
- La autenticación de Windows no está habilitada en SQL Server

**Solución:**
1. Verificar credenciales en SQL Server Management Studio
2. Asegurarse de que el usuario tiene permisos en la base de datos SOF108
3. Intentar con autenticación de Windows si está disponible

### Error: "Cannot open database SOF108"

**Solución:**
- Verificar que la base de datos SOF108 existe en SQL Server
- Verificar que el usuario tiene acceso a esa base de datos

### Error: "No se puede conectar al servidor"

**Causas posibles:**
- Nombre del servidor incorrecto
- SQL Server no está ejecutándose
- Firewall bloqueando la conexión
- TCP/IP no habilitado en SQL Server

**Solución:**
1. Verificar que SQL Server está ejecutándose (Services.msc → SQL Server)
2. Verificar el nombre del servidor en SSMS
3. Para instancias con nombre, usar formato: `SERVIDOR\INSTANCIA`
4. Habilitar TCP/IP en SQL Server Configuration Manager

### Error al importar CustomTkinter

**Solución:**
```bash
pip install --upgrade customtkinter
```

## 📁 Estructura del Proyecto

```
CRUD_empleados_sof_108/
│
├── config/                      # Configuración
│   ├── __init__.py
│   ├── database_config.py       # Config de BD
│   └── ui_config.py             # Colores y estilos
│
├── database/                    # Capa de datos
│   ├── __init__.py
│   ├── connection.py            # Conexión a SQL Server
│   └── crud_operations.py       # Operaciones CRUD
│
├── ui/                          # Interfaz gráfica
│   ├── __init__.py
│   ├── main_window.py           # Ventana principal
│   ├── sidebar.py               # Menú lateral
│   ├── data_table.py            # Tabla de datos
│   ├── forms.py                 # Formularios CRUD
│   ├── dialogs.py               # Diálogos
│   └── styles.py                # Estilos
│
├── utils/                       # Utilidades
│   ├── __init__.py
│   └── validators.py            # Validaciones
│
├── main.py                      # Punto de entrada
├── requirements.txt             # Dependencias
└── README.md                    # Documentación
```

## 🎨 Capturas de Pantalla

### Ventana de Configuración
![Configuración](docs/config.png)

### Ventana Principal - Empleados
![Empleados](docs/empleados.png)

### Formulario de Agregar
![Formulario](docs/formulario.png)

### Tema Claro
![Tema Claro](docs/tema_claro.png)

## ⌨️ Atajos de Teclado

- `Ctrl + R` - Actualizar datos
- `Ctrl + F` - Enfocar búsqueda
- `Delete` - Eliminar registro seleccionado
- `Enter` - Confirmar en diálogos
- `Esc` - Cancelar en diálogos

## 🔐 Seguridad

- Las contraseñas se almacenan localmente en `db_config.json`
- **IMPORTANTE**: No compartir el archivo `db_config.json` ya que contiene credenciales
- Para producción, considerar encriptar las credenciales

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## 📝 Notas Adicionales

### Validaciones Implementadas

- **Campos obligatorios**: Marcados con asterisco (*)
- **Formato de email**: Validación de formato correcto
- **Rangos de salario**: Salario mínimo < Salario máximo
- **Claves foráneas**: Solo valores existentes en tablas relacionadas
- **Tipos de datos**: Validación de números, fechas, etc.

### Relaciones entre Tablas

```
REGIONES (1) ──→ (N) PAISES
PAISES (1) ──→ (N) LOCACIONES
LOCACIONES (1) ──→ (N) DEPARTAMENTOS
DEPARTAMENTOS (1) ──→ (N) EMPLEADOS
PUESTOS (1) ──→ (N) EMPLEADOS
EMPLEADOS (1) ──→ (N) HISTORICO
```

### Limitaciones Conocidas

- La tabla HISTORICO no permite edición (solo agregar)
- No se puede eliminar un registro si tiene dependencias en otras tablas
- La búsqueda es sensible a mayúsculas/minúsculas

## 📞 Soporte

Para problemas o preguntas:

1. Revisar la sección de **Solución de Problemas**
2. Verificar que todos los requisitos estén instalados
3. Consultar la documentación de SQL Server

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 🙏 Agradecimientos

- **CustomTkinter** por la librería de UI moderna
- **pyodbc** por la conexión a SQL Server
- Comunidad de Python por las excelentes herramientas

---

**Desarrollado con ❤️ usando Python y CustomTkinter**

**Versión**: 1.0.0  
**Última actualización**: 2024
