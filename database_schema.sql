-- =============================================
-- Script de Creación de Base de Datos SOF108
-- Sistema de Gestión de Empleados
-- =============================================

-- Crear base de datos (si no existe)
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'SOF108')
BEGIN
    CREATE DATABASE SOF108;
END
GO

USE SOF108;
GO

-- =============================================
-- Tabla: REGIONES
-- =============================================
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'REGIONES')
BEGIN
    CREATE TABLE REGIONES (
        ID_REGION INT PRIMARY KEY IDENTITY(1,1),
        NOMBRE_REGION VARCHAR(25) NOT NULL
    );
END
GO

-- =============================================
-- Tabla: PAISES
-- =============================================
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'PAISES')
BEGIN
    CREATE TABLE PAISES (
        ID_PAIS VARCHAR(2) PRIMARY KEY,
        NOMBRE_PAIS VARCHAR(40) NOT NULL,
        ID_REGION INT,
        FOREIGN KEY (ID_REGION) REFERENCES REGIONES(ID_REGION)
    );
END
GO

-- =============================================
-- Tabla: LOCACIONES
-- =============================================
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'LOCACIONES')
BEGIN
    CREATE TABLE LOCACIONES (
        ID_LOCACION INT PRIMARY KEY IDENTITY(1,1),
        DIRECCION VARCHAR(40),
        CODIGO_POSTAL VARCHAR(12),
        CIUDAD VARCHAR(30) NOT NULL,
        PROVINCIA VARCHAR(25),
        ID_PAIS VARCHAR(2),
        FOREIGN KEY (ID_PAIS) REFERENCES PAISES(ID_PAIS)
    );
END
GO

-- =============================================
-- Tabla: DEPARTAMENTOS
-- =============================================
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'DEPARTAMENTOS')
BEGIN
    CREATE TABLE DEPARTAMENTOS (
        ID_DEPARTAMENTO INT PRIMARY KEY IDENTITY(1,1),
        NOMBRE_DEPARTAMENTO VARCHAR(30) NOT NULL,
        ID_SUPERVISOR INT,
        ID_LOCACION INT,
        FOREIGN KEY (ID_LOCACION) REFERENCES LOCACIONES(ID_LOCACION)
    );
END
GO

-- =============================================
-- Tabla: PUESTOS
-- =============================================
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'PUESTOS')
BEGIN
    CREATE TABLE PUESTOS (
        ID_PUESTO VARCHAR(10) PRIMARY KEY,
        TITULO_PUESTO VARCHAR(35) NOT NULL,
        SALARIO_MINIMO INT,
        SALARIO_MAXIMO INT
    );
END
GO

-- =============================================
-- Tabla: EMPLEADOS
-- =============================================
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'EMPLEADOS')
BEGIN
    CREATE TABLE EMPLEADOS (
        ID_EMPLEADO INT PRIMARY KEY IDENTITY(1,1),
        NOMBRE VARCHAR(20) NOT NULL,
        APELLIDO VARCHAR(25) NOT NULL,
        EMAIL VARCHAR(25) NOT NULL,
        NUMERO_TELEFONO VARCHAR(20),
        FECHA_CONTRATO DATETIME NOT NULL,
        ID_PUESTO VARCHAR(10),
        SALARIO INT,
        COMISION INT,
        ID_SUPERVISOR INT,
        ID_DEPARTAMENTO INT,
        FOREIGN KEY (ID_PUESTO) REFERENCES PUESTOS(ID_PUESTO),
        FOREIGN KEY (ID_DEPARTAMENTO) REFERENCES DEPARTAMENTOS(ID_DEPARTAMENTO)
    );
END
GO

-- =============================================
-- Tabla: HISTORICO
-- =============================================
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'HISTORICO')
BEGIN
    CREATE TABLE HISTORICO (
        ID_EMPLEADO INT,
        FECHA_INICIO DATETIME NOT NULL,
        FECHA_FIN DATETIME NOT NULL,
        ID_PUESTO VARCHAR(10),
        ID_DEPARTAMENTO INT,
        PRIMARY KEY (ID_EMPLEADO, FECHA_INICIO),
        FOREIGN KEY (ID_EMPLEADO) REFERENCES EMPLEADOS(ID_EMPLEADO),
        FOREIGN KEY (ID_PUESTO) REFERENCES PUESTOS(ID_PUESTO),
        FOREIGN KEY (ID_DEPARTAMENTO) REFERENCES DEPARTAMENTOS(ID_DEPARTAMENTO)
    );
END
GO

-- =============================================
-- Datos de Ejemplo (Opcional)
-- =============================================

-- Insertar regiones de ejemplo
IF NOT EXISTS (SELECT * FROM REGIONES)
BEGIN
    INSERT INTO REGIONES (NOMBRE_REGION) VALUES 
        ('Europa'),
        ('América'),
        ('Asia'),
        ('África');
END
GO

-- Insertar países de ejemplo
IF NOT EXISTS (SELECT * FROM PAISES)
BEGIN
    INSERT INTO PAISES (ID_PAIS, NOMBRE_PAIS, ID_REGION) VALUES 
        ('ES', 'España', 1),
        ('US', 'Estados Unidos', 2),
        ('MX', 'México', 2),
        ('AR', 'Argentina', 2),
        ('JP', 'Japón', 3);
END
GO

-- Insertar locaciones de ejemplo
IF NOT EXISTS (SELECT * FROM LOCACIONES)
BEGIN
    INSERT INTO LOCACIONES (DIRECCION, CODIGO_POSTAL, CIUDAD, PROVINCIA, ID_PAIS) VALUES 
        ('Calle Mayor 1', '28001', 'Madrid', 'Madrid', 'ES'),
        ('5th Avenue 100', '10001', 'New York', 'New York', 'US'),
        ('Reforma 500', '06600', 'Ciudad de México', 'CDMX', 'MX');
END
GO

-- Insertar puestos de ejemplo
IF NOT EXISTS (SELECT * FROM PUESTOS)
BEGIN
    INSERT INTO PUESTOS (ID_PUESTO, TITULO_PUESTO, SALARIO_MINIMO, SALARIO_MAXIMO) VALUES 
        ('IT_PROG', 'Programador', 30000, 60000),
        ('IT_MGR', 'Gerente de TI', 60000, 100000),
        ('HR_REP', 'Representante de RRHH', 25000, 45000),
        ('SALES', 'Vendedor', 20000, 50000),
        ('ADMIN', 'Administrativo', 18000, 35000);
END
GO

-- Insertar departamentos de ejemplo
IF NOT EXISTS (SELECT * FROM DEPARTAMENTOS)
BEGIN
    INSERT INTO DEPARTAMENTOS (NOMBRE_DEPARTAMENTO, ID_SUPERVISOR, ID_LOCACION) VALUES 
        ('Tecnología', NULL, 1),
        ('Recursos Humanos', NULL, 1),
        ('Ventas', NULL, 2),
        ('Administración', NULL, 1);
END
GO

PRINT '✅ Base de datos SOF108 creada exitosamente';
PRINT '✅ Todas las tablas han sido creadas';
PRINT '✅ Datos de ejemplo insertados';
GO
