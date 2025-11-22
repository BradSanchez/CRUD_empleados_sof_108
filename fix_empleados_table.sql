-- =============================================
-- Script para Corregir Tabla EMPLEADOS
-- Agrega IDENTITY a ID_EMPLEADO
-- =============================================

USE SOF108;
GO

-- Verificar si la tabla existe
IF EXISTS (SELECT * FROM sys.tables WHERE name = 'EMPLEADOS')
BEGIN
    PRINT 'Corrigiendo tabla EMPLEADOS...';
    
    -- Eliminar restricciones de clave foránea que apuntan a EMPLEADOS
    IF EXISTS (SELECT * FROM sys.foreign_keys WHERE name = 'FK__HISTORICO__ID_EM__5AEE82B9')
        ALTER TABLE HISTORICO DROP CONSTRAINT FK__HISTORICO__ID_EM__5AEE82B9;
    
    -- Crear tabla temporal con la estructura correcta
    CREATE TABLE EMPLEADOS_TEMP (
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
    
    -- Copiar datos existentes (si hay)
    IF EXISTS (SELECT * FROM EMPLEADOS)
    BEGIN
        SET IDENTITY_INSERT EMPLEADOS_TEMP ON;
        
        INSERT INTO EMPLEADOS_TEMP (ID_EMPLEADO, NOMBRE, APELLIDO, EMAIL, NUMERO_TELEFONO, 
                                    FECHA_CONTRATO, ID_PUESTO, SALARIO, COMISION, 
                                    ID_SUPERVISOR, ID_DEPARTAMENTO)
        SELECT ID_EMPLEADO, NOMBRE, APELLIDO, EMAIL, NUMERO_TELEFONO, 
               FECHA_CONTRATO, ID_PUESTO, SALARIO, COMISION, 
               ID_SUPERVISOR, ID_DEPARTAMENTO
        FROM EMPLEADOS;
        
        SET IDENTITY_INSERT EMPLEADOS_TEMP OFF;
    END
    
    -- Eliminar tabla antigua
    DROP TABLE EMPLEADOS;
    
    -- Renombrar tabla temporal
    EXEC sp_rename 'EMPLEADOS_TEMP', 'EMPLEADOS';
    
    -- Recrear restricción de clave foránea en HISTORICO
    ALTER TABLE HISTORICO 
    ADD CONSTRAINT FK_HISTORICO_EMPLEADOS 
    FOREIGN KEY (ID_EMPLEADO) REFERENCES EMPLEADOS(ID_EMPLEADO);
    
    PRINT '✅ Tabla EMPLEADOS corregida exitosamente';
    PRINT '✅ ID_EMPLEADO ahora tiene IDENTITY(1,1)';
END
ELSE
BEGIN
    PRINT '❌ La tabla EMPLEADOS no existe';
END
GO
