# 📚 Ejemplos de Uso - CRUD SOF108

Esta guía proporciona ejemplos prácticos de cómo usar la aplicación para tareas comunes.

## 🎯 Escenarios Comunes

### Escenario 1: Agregar un Nuevo Empleado

**Situación**: Contratar a un nuevo empleado llamado Juan Pérez como Programador.

**Pasos**:

1. **Preparar datos previos** (si no existen):
   - Crear región "América"
   - Crear país "México" en región América
   - Crear locación en Ciudad de México
   - Crear departamento "Tecnología"
   - Crear puesto "IT_PROG - Programador"

2. **Agregar el empleado**:
   - Click en "👥 Empleados" en el menú lateral
   - Click en "➕ Agregar"
   - Completar formulario:
     ```
     Nombre: Juan
     Apellido: Pérez
     Email: juan.perez@empresa.com
     Teléfono: +52 55 1234 5678
     Fecha de Contrato: 2024-01-15
     Puesto: IT_PROG - Programador
     Salario: 45000
     Comisión: (dejar vacío)
     Supervisor: (seleccionar si existe)
     Departamento: Tecnología
     ```
   - Click en "💾 Guardar"

3. **Verificar**:
   - El nuevo empleado aparecerá en la tabla
   - Usar búsqueda para encontrarlo: escribir "Juan"

---

### Escenario 2: Actualizar Salario de un Empleado

**Situación**: Juan Pérez recibe un aumento de salario.

**Pasos**:

1. Click en "👥 Empleados"
2. Buscar "Juan Pérez" en el campo de búsqueda
3. Seleccionar la fila de Juan Pérez
4. Click en "✏️ Editar"
5. Modificar el campo "Salario": cambiar de 45000 a 50000
6. Click en "💾 Guardar"
7. Verificar que el cambio se refleja en la tabla

---

### Escenario 3: Registrar Cambio de Departamento

**Situación**: Juan Pérez se transfiere del departamento de Tecnología a Ventas.

**Pasos**:

1. **Registrar en histórico** (antes de cambiar):
   - Click en "📜 Histórico"
   - Click en "➕ Agregar"
   - Completar:
     ```
     Empleado: Juan Pérez
     Fecha Inicio: 2024-01-15 (fecha de contrato original)
     Fecha Fin: 2024-06-30 (último día en Tecnología)
     Puesto: IT_PROG - Programador
     Departamento: Tecnología
     ```
   - Click en "💾 Guardar"

2. **Actualizar empleado**:
   - Click en "👥 Empleados"
   - Buscar y seleccionar a Juan Pérez
   - Click en "✏️ Editar"
   - Cambiar:
     ```
     Puesto: SALES - Vendedor
     Departamento: Ventas
     Fecha de Contrato: 2024-07-01 (nueva fecha)
     ```
   - Click en "💾 Guardar"

---

### Escenario 4: Crear Estructura Organizacional Completa

**Situación**: Configurar una nueva oficina en España.

**Pasos**:

1. **Crear Región** (si no existe):
   - Click en "📊 Regiones"
   - Click en "➕ Agregar"
   - Nombre: "Europa"
   - Guardar

2. **Crear País**:
   - Click en "🌍 Países"
   - Click en "➕ Agregar"
   - Código: "ES"
   - Nombre: "España"
   - Región: "Europa"
   - Guardar

3. **Crear Locación**:
   - Click en "📍 Locaciones"
   - Click en "➕ Agregar"
   - Dirección: "Gran Vía 28"
   - Código Postal: "28013"
   - Ciudad: "Madrid"
   - Provincia: "Madrid"
   - País: "ES - España"
   - Guardar

4. **Crear Departamento**:
   - Click en "🏢 Departamentos"
   - Click en "➕ Agregar"
   - Nombre: "Ventas España"
   - Supervisor: (dejar vacío por ahora)
   - Locación: "Madrid"
   - Guardar

5. **Crear Puestos**:
   - Click en "💼 Puestos"
   - Agregar varios puestos:
     ```
     Código: SALES_ES
     Título: Vendedor España
     Salario Mínimo: 25000
     Salario Máximo: 45000
     ```

6. **Agregar Empleados**:
   - Click en "👥 Empleados"
   - Agregar empleados para la oficina de Madrid

---

### Escenario 5: Buscar y Filtrar Información

**Situación**: Encontrar todos los empleados del departamento de Tecnología.

**Pasos**:

1. Click en "👥 Empleados"
2. En el campo de búsqueda, escribir: "Tecnología"
3. La tabla se filtrará automáticamente mostrando solo empleados de ese departamento

**Otros ejemplos de búsqueda**:
- Buscar por nombre: "Juan"
- Buscar por email: "@empresa.com"
- Buscar por puesto: "Programador"
- Buscar por salario: "45000"

---

### Escenario 6: Eliminar un Registro

**Situación**: Eliminar un país que ya no se usa.

**Pasos**:

1. **Verificar dependencias**:
   - Asegurarse de que no hay locaciones en ese país
   - Si hay locaciones, eliminarlas primero

2. **Eliminar el país**:
   - Click en "🌍 Países"
   - Seleccionar el país a eliminar
   - Click en "🗑️ Eliminar"
   - Confirmar en el diálogo

**Nota**: Si hay dependencias, aparecerá un error. Eliminar primero los registros dependientes.

---

### Escenario 7: Reconfigurar Conexión a Base de Datos

**Situación**: Cambiar de servidor de base de datos.

**Pasos**:

1. Click en "⚙️ Configuración" en el menú lateral
2. Modificar los datos:
   ```
   Servidor: nuevo-servidor\SQLEXPRESS
   Autenticación: SQL Server
   Usuario: sa
   Contraseña: ********
   ```
3. Click en "🔍 Probar Conexión"
4. Si es exitoso, click en "💾 Guardar y Conectar"
5. La aplicación se reconectará automáticamente

---

### Escenario 8: Cambiar Tema Visual

**Situación**: Preferir trabajar con tema claro durante el día.

**Pasos**:

1. Click en "🌓 Cambiar Tema" en el menú lateral
2. La interfaz cambiará inmediatamente entre modo oscuro y claro
3. El cambio se aplica a toda la aplicación

---

## 🔍 Casos de Uso Avanzados

### Gestión de Jerarquía de Empleados

**Crear estructura de supervisión**:

1. Agregar gerente sin supervisor:
   ```
   Nombre: María
   Apellido: García
   Puesto: IT_MGR - Gerente de TI
   Supervisor: (vacío)
   ```

2. Agregar empleados bajo ese gerente:
   ```
   Nombre: Juan
   Apellido: Pérez
   Puesto: IT_PROG - Programador
   Supervisor: María García
   ```

### Gestión de Comisiones

**Para empleados de ventas**:

1. Crear puesto con comisión:
   ```
   Código: SALES
   Título: Vendedor
   Salario Mínimo: 20000
   Salario Máximo: 35000
   ```

2. Agregar empleado con comisión:
   ```
   Nombre: Carlos
   Puesto: SALES - Vendedor
   Salario: 25000
   Comisión: 5000
   ```

### Seguimiento de Historial Laboral

**Registrar toda la trayectoria de un empleado**:

1. Cada vez que cambie de puesto o departamento
2. Agregar registro en "📜 Histórico"
3. Actualizar datos actuales en "👥 Empleados"

---

## ⚠️ Errores Comunes y Soluciones

### Error: "El campo es obligatorio"

**Causa**: No se completó un campo marcado con *

**Solución**: Completar todos los campos obligatorios antes de guardar

### Error: "El salario mínimo debe ser menor al máximo"

**Causa**: Valores de salario incorrectos en puestos

**Solución**: Verificar que Salario Mínimo < Salario Máximo

### Error: "No se puede eliminar el registro"

**Causa**: Existen registros dependientes en otras tablas

**Solución**: 
1. Identificar las dependencias
2. Eliminar primero los registros dependientes
3. Luego eliminar el registro principal

### Error: "Formato de email inválido"

**Causa**: Email no tiene formato correcto

**Solución**: Usar formato: usuario@dominio.com

---

## 💡 Consejos y Mejores Prácticas

### Organización de Datos

1. **Crear estructura de arriba hacia abajo**:
   - Primero: Regiones
   - Segundo: Países
   - Tercero: Locaciones
   - Cuarto: Departamentos y Puestos
   - Quinto: Empleados
   - Sexto: Histórico

2. **Usar códigos consistentes**:
   - Puestos: IT_PROG, IT_MGR, HR_REP
   - Países: ES, US, MX (ISO 3166-1 alpha-2)

3. **Mantener histórico actualizado**:
   - Registrar cambios antes de modificar empleados
   - Incluir fechas exactas

### Búsqueda Eficiente

1. **Usar términos específicos**:
   - En lugar de "a", buscar "admin"
   - En lugar de "2", buscar "2024"

2. **Buscar por diferentes campos**:
   - Nombre, apellido, email, departamento, etc.

3. **Actualizar datos regularmente**:
   - Click en "🔄 Actualizar" para ver cambios recientes

### Mantenimiento

1. **Backup regular**:
   - Hacer backup de la base de datos SOF108 en SSMS
   - Guardar archivo db_config.json

2. **Verificar integridad**:
   - Revisar que no haya registros huérfanos
   - Verificar relaciones entre tablas

3. **Limpiar datos obsoletos**:
   - Eliminar registros que ya no se usan
   - Mantener solo datos relevantes

---

## 📊 Flujos de Trabajo Recomendados

### Flujo: Contratación de Empleado

```
1. Verificar que existe:
   ├─ Región
   ├─ País
   ├─ Locación
   ├─ Departamento
   └─ Puesto

2. Agregar empleado con todos los datos

3. Asignar supervisor (si aplica)

4. Verificar en la tabla de empleados
```

### Flujo: Promoción de Empleado

```
1. Registrar en histórico:
   └─ Puesto anterior, departamento, fechas

2. Actualizar empleado:
   ├─ Nuevo puesto
   ├─ Nuevo salario
   └─ Nuevo departamento (si aplica)

3. Verificar cambios
```

### Flujo: Apertura de Nueva Oficina

```
1. Crear locación

2. Crear departamentos para esa locación

3. Crear puestos específicos (si aplica)

4. Contratar empleados

5. Asignar supervisores
```

---

**¿Necesitas más ejemplos?** Consulta el README.md para más información. 📚
