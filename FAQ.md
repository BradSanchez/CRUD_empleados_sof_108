# ❓ Preguntas Frecuentes (FAQ) - CRUD SOF108

Respuestas a las preguntas más comunes sobre la aplicación.

## 📦 Instalación y Configuración

### ¿Qué versión de Python necesito?

Python 3.8 o superior. Verificar con:
```bash
python --version
```

### ¿Funciona con SQL Server Express?

Sí, funciona perfectamente con SQL Server Express (versión gratuita).

### ¿Necesito instalar algo más además de Python?

Sí, necesitas:
1. SQL Server (cualquier versión)
2. ODBC Driver 17 for SQL Server
3. Las dependencias de Python (instaladas con `pip install -r requirements.txt`)

### ¿Dónde descargo ODBC Driver 17?

https://docs.microsoft.com/sql/connect/odbc/download-odbc-driver-for-sql-server

### ¿Puedo usar otro driver ODBC?

Sí, si no tienes ODBC Driver 17, la aplicación intentará usar el driver "SQL Server" genérico.

---

## 🔌 Conexión a Base de Datos

### ¿Cómo sé el nombre de mi servidor SQL Server?

1. Abrir SQL Server Management Studio (SSMS)
2. Al conectarte, el nombre aparece en el campo "Server name"
3. Ejemplos comunes:
   - `localhost`
   - `.\SQLEXPRESS`
   - `MIPC\SQLEXPRESS`
   - `192.168.1.100`

### ¿Qué tipo de autenticación debo usar?

- **Windows Authentication**: Recomendado si SQL Server está en tu PC
- **SQL Server Authentication**: Si necesitas usuario y contraseña específicos

### ¿Dónde se guarda la configuración de conexión?

En el archivo `db_config.json` en la carpeta del proyecto.

### ¿Es seguro guardar la contraseña en el archivo?

El archivo se guarda localmente. Para mayor seguridad:
- No compartir el archivo `db_config.json`
- Usar autenticación de Windows cuando sea posible
- Establecer permisos adecuados en la carpeta

### ¿Puedo conectarme a un servidor remoto?

Sí, usa la IP o nombre del servidor remoto. Asegúrate de que:
- SQL Server permite conexiones remotas
- El firewall permite el puerto 1433
- Tienes credenciales válidas

### Error: "Cannot open database SOF108"

**Causas**:
- La base de datos no existe
- No tienes permisos

**Solución**:
1. Verificar en SSMS que SOF108 existe
2. Ejecutar el script `database_schema.sql` si no existe
3. Verificar permisos del usuario

---

## 🎨 Interfaz y Uso

### ¿Cómo cambio entre tema claro y oscuro?

Click en "🌓 Cambiar Tema" en el menú lateral inferior.

### ¿Puedo redimensionar la ventana?

Sí, la ventana es completamente redimensionable. Arrastra desde los bordes.

### ¿Cómo busco un registro específico?

Escribe en el campo de búsqueda sobre la tabla. La búsqueda filtra en tiempo real.

### ¿La búsqueda distingue mayúsculas y minúsculas?

No, la búsqueda no es sensible a mayúsculas/minúsculas.

### ¿Puedo ordenar las columnas?

En la versión actual no, pero está planeado para versiones futuras.

### ¿Cómo selecciono un registro para editar?

Click en la fila de la tabla para seleccionarla, luego click en "✏️ Editar".

### ¿Puedo editar directamente en la tabla?

No, debes usar el botón "✏️ Editar" que abre un formulario.

---

## 📝 Operaciones CRUD

### ¿Qué campos son obligatorios?

Los campos marcados con asterisco (*) son obligatorios.

### ¿Puedo dejar campos vacíos?

Solo los campos sin asterisco pueden dejarse vacíos (opcionales).

### ¿Por qué no puedo editar el histórico?

Por diseño, el histórico es solo de lectura. Solo se pueden agregar registros nuevos.

### ¿Puedo eliminar cualquier registro?

Solo si no tiene dependencias en otras tablas. Por ejemplo:
- No puedes eliminar un país si tiene locaciones
- No puedes eliminar un departamento si tiene empleados

### ¿Cómo elimino un registro con dependencias?

1. Primero elimina los registros dependientes
2. Luego elimina el registro principal

Ejemplo: Para eliminar un país, primero elimina todas sus locaciones.

### ¿Los cambios se guardan automáticamente?

No, debes hacer click en "💾 Guardar" en los formularios.

### ¿Puedo deshacer un cambio?

No hay función de deshacer. Se recomienda hacer backups regulares de la base de datos.

---

## 🔧 Problemas Técnicos

### La aplicación no inicia

**Verificar**:
1. Python está instalado: `python --version`
2. Dependencias instaladas: `pip list`
3. Ejecutar: `python test_installation.py`

### Error: "No module named 'pyodbc'"

```bash
pip install pyodbc
```

### Error: "No module named 'customtkinter'"

```bash
pip install customtkinter
```

### La ventana aparece en blanco

**Posibles causas**:
- Problema con CustomTkinter
- Drivers gráficos desactualizados

**Solución**:
```bash
pip install --upgrade customtkinter
```

### Los botones no responden

Reiniciar la aplicación. Si persiste, verificar la conexión a la base de datos.

### La búsqueda no funciona

Verificar que hay datos en la tabla. Si la tabla está vacía, la búsqueda no mostrará resultados.

### Error al guardar: "Violation of PRIMARY KEY constraint"

Estás intentando agregar un registro con un ID que ya existe. Usa un ID diferente.

### Error: "The INSERT statement conflicted with the FOREIGN KEY constraint"

Estás intentando agregar un registro con una clave foránea que no existe.

**Ejemplo**: Agregar un empleado con un departamento que no existe.

**Solución**: Primero crea el registro relacionado (departamento), luego el empleado.

---

## 💾 Base de Datos

### ¿Puedo usar otra base de datos además de SOF108?

Sí, pero debes modificar el código en `database_config.py` para cambiar el nombre de la base de datos.

### ¿Cómo hago backup de mis datos?

En SQL Server Management Studio:
1. Click derecho en la base de datos SOF108
2. Tasks → Back Up...
3. Seleccionar ubicación y hacer backup

### ¿Puedo importar datos desde Excel?

No directamente en la versión actual. Está planeado para versiones futuras.

**Alternativa**: Importar en SSMS usando el asistente de importación.

### ¿Puedo exportar los datos?

No directamente en la versión actual. Está planeado para versiones futuras.

**Alternativa**: Copiar datos desde la tabla y pegar en Excel.

### ¿La aplicación modifica la estructura de la base de datos?

No, solo realiza operaciones CRUD (INSERT, SELECT, UPDATE, DELETE). No modifica tablas.

### ¿Puedo usar la aplicación con una base de datos existente?

Sí, siempre que tenga la estructura correcta (las 7 tablas con los campos especificados).

---

## 🚀 Rendimiento

### ¿Cuántos registros puede manejar?

La aplicación puede manejar miles de registros. El límite depende de:
- Capacidad de SQL Server
- Memoria RAM disponible
- Velocidad de la red (si es servidor remoto)

### La aplicación va lenta con muchos datos

**Optimizaciones**:
1. Usar búsqueda para filtrar datos
2. Agregar índices en SQL Server
3. Cerrar otras aplicaciones

### ¿Puedo usar la aplicación en red?

Sí, múltiples usuarios pueden conectarse al mismo servidor SQL Server.

**Nota**: No hay control de concurrencia avanzado. Evitar que múltiples usuarios editen el mismo registro simultáneamente.

---

## 🔐 Seguridad

### ¿Es segura la aplicación?

La aplicación usa:
- Consultas parametrizadas (previene SQL injection)
- Validación de entrada
- Conexiones seguras a SQL Server

### ¿Dónde se guardan las contraseñas?

En el archivo `db_config.json` en texto plano. No compartir este archivo.

### ¿Puedo encriptar las contraseñas?

No en la versión actual. Está planeado para versiones futuras.

### ¿Hay registro de auditoría?

No en la versión actual. Está planeado para versiones futuras.

### ¿Puedo restringir acceso a ciertas tablas?

No en la aplicación. Puedes configurar permisos en SQL Server.

---

## 🎯 Funcionalidades

### ¿Puedo agregar más tablas?

Sí, pero requiere modificar el código:
1. Agregar operaciones CRUD en `crud_operations.py`
2. Crear formulario en `forms.py`
3. Agregar opción en el menú lateral

### ¿Puedo personalizar los colores?

Sí, modificar `config/ui_config.py` para cambiar colores.

### ¿Puedo agregar más validaciones?

Sí, modificar `utils/validators.py` y los formularios en `ui/forms.py`.

### ¿Hay atajos de teclado?

Actualmente limitados. Planeados para versiones futuras:
- Ctrl+R: Actualizar
- Ctrl+F: Buscar
- Delete: Eliminar

### ¿Puedo generar reportes?

No en la versión actual. Está planeado para versiones futuras.

---

## 📱 Compatibilidad

### ¿Funciona en Windows?

Sí, completamente compatible con Windows 10 y 11.

### ¿Funciona en Mac?

Sí, pero necesitas:
- Instalar Python para Mac
- Instalar ODBC Driver para Mac
- Ajustar rutas en el código si es necesario

### ¿Funciona en Linux?

Sí, con las mismas consideraciones que Mac.

### ¿Hay versión web?

No, es una aplicación de escritorio. Una versión web está en el roadmap.

### ¿Hay versión móvil?

No, solo escritorio.

---

## 🆘 Soporte

### ¿Dónde encuentro más ayuda?

1. Leer `README.md`
2. Leer `INSTALACION.md`
3. Revisar `EJEMPLOS_USO.md`
4. Ejecutar `python test_installation.py`

### ¿Cómo reporto un bug?

Crear un issue en el repositorio con:
- Descripción del problema
- Pasos para reproducir
- Mensaje de error (si hay)
- Versión de Python y sistema operativo

### ¿Puedo contribuir al proyecto?

Sí, las contribuciones son bienvenidas. Ver sección de contribuciones en README.md.

### ¿Hay actualizaciones?

Revisar `CHANGELOG.md` para ver el historial de versiones.

---

## 💡 Consejos

### Mejores prácticas

1. **Hacer backups regulares** de la base de datos
2. **Usar autenticación de Windows** cuando sea posible
3. **Mantener Python actualizado**
4. **Verificar datos antes de eliminar**
5. **Usar búsqueda para encontrar registros rápidamente**

### Optimización

1. **Cerrar la aplicación** cuando no la uses
2. **Actualizar datos** regularmente con el botón 🔄
3. **Limpiar datos obsoletos** periódicamente
4. **Usar filtros** en lugar de cargar todos los datos

### Solución rápida de problemas

1. **Reiniciar la aplicación**
2. **Verificar conexión a SQL Server**
3. **Ejecutar `python test_installation.py`**
4. **Revisar archivo `db_config.json`**
5. **Consultar logs de SQL Server**

---

## 📞 Contacto

¿Tienes más preguntas? Consulta la documentación completa en los archivos README.md e INSTALACION.md.

---

**Última actualización**: 2024  
**Versión**: 1.0.0
