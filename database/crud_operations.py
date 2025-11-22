class CRUDOperations:
    """Operaciones CRUD para todas las tablas"""
    
    def __init__(self, db_connection):
        self.db = db_connection
    
    # ==================== REGIONES ====================
    def get_regiones(self):
        query = "SELECT ID_REGION, NOMBRE_REGION FROM REGIONES ORDER BY ID_REGION"
        return self.db.execute_query(query)
    
    def add_region(self, nombre):
        query_max = "SELECT ISNULL(MAX(ID_REGION), 0) + 1 FROM REGIONES"
        success, cols, result = self.db.execute_query(query_max)
        if not success:
            return False, "Error al obtener ID"
        nuevo_id = result[0][0]
        query = "INSERT INTO REGIONES (ID_REGION, NOMBRE_REGION) VALUES (?, ?)"
        return self.db.execute_non_query(query, (nuevo_id, nombre))
    
    def update_region(self, id_region, nombre):
        query = "UPDATE REGIONES SET NOMBRE_REGION = ? WHERE ID_REGION = ?"
        return self.db.execute_non_query(query, (nombre, id_region))
    
    def delete_region(self, id_region):
        query = "DELETE FROM REGIONES WHERE ID_REGION = ?"
        return self.db.execute_non_query(query, (id_region,))
    
    # ==================== PAISES ====================
    def get_paises(self):
        query = """
        SELECT P.ID_PAIS, P.NOMBRE_PAIS, P.ID_REGION, R.NOMBRE_REGION
        FROM PAISES P
        LEFT JOIN REGIONES R ON P.ID_REGION = R.ID_REGION
        ORDER BY P.ID_PAIS
        """
        return self.db.execute_query(query)
    
    def add_pais(self, id_pais, nombre, id_region):
        query = "INSERT INTO PAISES (ID_PAIS, NOMBRE_PAIS, ID_REGION) VALUES (?, ?, ?)"
        return self.db.execute_non_query(query, (id_pais, nombre, id_region))
    
    def update_pais(self, id_pais, nombre, id_region):
        query = "UPDATE PAISES SET NOMBRE_PAIS = ?, ID_REGION = ? WHERE ID_PAIS = ?"
        return self.db.execute_non_query(query, (nombre, id_region, id_pais))
    
    def delete_pais(self, id_pais):
        query = "DELETE FROM PAISES WHERE ID_PAIS = ?"
        return self.db.execute_non_query(query, (id_pais,))
    
    # ==================== LOCACIONES ====================
    def get_locaciones(self):
        query = """
        SELECT L.ID_LOCACION, L.DIRECCION, L.CODIGO_POSTAL, L.CIUDAD, 
               L.PROVINCIA, L.ID_PAIS, P.NOMBRE_PAIS
        FROM LOCACIONES L
        LEFT JOIN PAISES P ON L.ID_PAIS = P.ID_PAIS
        ORDER BY L.ID_LOCACION
        """
        return self.db.execute_query(query)
    
    def add_locacion(self, direccion, codigo_postal, ciudad, provincia, id_pais):
        query_max = "SELECT ISNULL(MAX(ID_LOCACION), 0) + 1 FROM LOCACIONES"
        success, cols, result = self.db.execute_query(query_max)
        if not success:
            return False, "Error al obtener ID"
        nuevo_id = result[0][0]
        query = """
        INSERT INTO LOCACIONES (ID_LOCACION, DIRECCION, CODIGO_POSTAL, CIUDAD, PROVINCIA, ID_PAIS)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        return self.db.execute_non_query(query, (nuevo_id, direccion, codigo_postal, ciudad, provincia, id_pais))
    
    def update_locacion(self, id_locacion, direccion, codigo_postal, ciudad, provincia, id_pais):
        query = """
        UPDATE LOCACIONES 
        SET DIRECCION = ?, CODIGO_POSTAL = ?, CIUDAD = ?, PROVINCIA = ?, ID_PAIS = ?
        WHERE ID_LOCACION = ?
        """
        return self.db.execute_non_query(query, (direccion, codigo_postal, ciudad, provincia, id_pais, id_locacion))
    
    def delete_locacion(self, id_locacion):
        query = "DELETE FROM LOCACIONES WHERE ID_LOCACION = ?"
        return self.db.execute_non_query(query, (id_locacion,))
    
    # ==================== DEPARTAMENTOS ====================
    def get_departamentos(self):
        query = """
        SELECT D.ID_DEPARTAMENTO, D.NOMBRE_DEPARTAMENTO, D.ID_SUPERVISOR, 
               D.ID_LOCACION, L.CIUDAD
        FROM DEPARTAMENTOS D
        LEFT JOIN LOCACIONES L ON D.ID_LOCACION = L.ID_LOCACION
        ORDER BY D.ID_DEPARTAMENTO
        """
        return self.db.execute_query(query)
    
    def add_departamento(self, nombre, id_supervisor, id_locacion):
        query_max = "SELECT ISNULL(MAX(ID_DEPARTAMENTO), 0) + 1 FROM DEPARTAMENTOS"
        success, cols, result = self.db.execute_query(query_max)
        if not success:
            return False, "Error al obtener ID"
        nuevo_id = result[0][0]
        query = """
        INSERT INTO DEPARTAMENTOS (ID_DEPARTAMENTO, NOMBRE_DEPARTAMENTO, ID_SUPERVISOR, ID_LOCACION)
        VALUES (?, ?, ?, ?)
        """
        return self.db.execute_non_query(query, (nuevo_id, nombre, id_supervisor, id_locacion))
    
    def update_departamento(self, id_departamento, nombre, id_supervisor, id_locacion):
        query = """
        UPDATE DEPARTAMENTOS 
        SET NOMBRE_DEPARTAMENTO = ?, ID_SUPERVISOR = ?, ID_LOCACION = ?
        WHERE ID_DEPARTAMENTO = ?
        """
        return self.db.execute_non_query(query, (nombre, id_supervisor, id_locacion, id_departamento))
    
    def delete_departamento(self, id_departamento):
        query = "DELETE FROM DEPARTAMENTOS WHERE ID_DEPARTAMENTO = ?"
        return self.db.execute_non_query(query, (id_departamento,))
    
    # ==================== PUESTOS ====================
    def get_puestos(self):
        query = """
        SELECT ID_PUESTO, TITULO_PUESTO, SALARIO_MINIMO, SALARIO_MAXIMO
        FROM PUESTOS
        ORDER BY ID_PUESTO
        """
        return self.db.execute_query(query)
    
    def add_puesto(self, id_puesto, titulo, salario_min, salario_max):
        query = """
        INSERT INTO PUESTOS (ID_PUESTO, TITULO_PUESTO, SALARIO_MINIMO, SALARIO_MAXIMO)
        VALUES (?, ?, ?, ?)
        """
        return self.db.execute_non_query(query, (id_puesto, titulo, salario_min, salario_max))
    
    def update_puesto(self, id_puesto, titulo, salario_min, salario_max):
        query = """
        UPDATE PUESTOS 
        SET TITULO_PUESTO = ?, SALARIO_MINIMO = ?, SALARIO_MAXIMO = ?
        WHERE ID_PUESTO = ?
        """
        return self.db.execute_non_query(query, (titulo, salario_min, salario_max, id_puesto))
    
    def delete_puesto(self, id_puesto):
        query = "DELETE FROM PUESTOS WHERE ID_PUESTO = ?"
        return self.db.execute_non_query(query, (id_puesto,))
    
    # ==================== EMPLEADOS ====================
    def get_empleados(self):
        query = """
        SELECT E.ID_EMPLEADO, E.NOMBRE, E.APELLIDO, E.EMAIL, E.NUMERO_TELEFONO,
               E.FECHA_CONTRATO, E.ID_PUESTO, P.TITULO_PUESTO, E.SALARIO, E.COMISION,
               E.ID_SUPERVISOR, E.ID_DEPARTAMENTO, D.NOMBRE_DEPARTAMENTO
        FROM EMPLEADOS E
        LEFT JOIN PUESTOS P ON E.ID_PUESTO = P.ID_PUESTO
        LEFT JOIN DEPARTAMENTOS D ON E.ID_DEPARTAMENTO = D.ID_DEPARTAMENTO
        ORDER BY E.ID_EMPLEADO
        """
        return self.db.execute_query(query)
    
    def add_empleado(self, nombre, apellido, email, telefono, fecha_contrato, 
                     id_puesto, salario, comision, id_supervisor, id_departamento):
        # Obtener el siguiente ID
        query_max = "SELECT ISNULL(MAX(ID_EMPLEADO), 0) + 1 FROM EMPLEADOS"
        success, cols, result = self.db.execute_query(query_max)
        if not success:
            return False, "Error al obtener ID"
        
        nuevo_id = result[0][0]
        
        query = """
        INSERT INTO EMPLEADOS 
        (ID_EMPLEADO, NOMBRE, APELLIDO, EMAIL, NUMERO_TELEFONO, FECHA_CONTRATO, ID_PUESTO, 
         SALARIO, COMISION, ID_SUPERVISOR, ID_DEPARTAMENTO)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        return self.db.execute_non_query(query, (nuevo_id, nombre, apellido, email, telefono, 
                                                  fecha_contrato, id_puesto, salario, 
                                                  comision, id_supervisor, id_departamento))
    
    def update_empleado(self, id_empleado, nombre, apellido, email, telefono, 
                        fecha_contrato, id_puesto, salario, comision, id_supervisor, id_departamento):
        query = """
        UPDATE EMPLEADOS 
        SET NOMBRE = ?, APELLIDO = ?, EMAIL = ?, NUMERO_TELEFONO = ?, 
            FECHA_CONTRATO = ?, ID_PUESTO = ?, SALARIO = ?, COMISION = ?,
            ID_SUPERVISOR = ?, ID_DEPARTAMENTO = ?
        WHERE ID_EMPLEADO = ?
        """
        return self.db.execute_non_query(query, (nombre, apellido, email, telefono, 
                                                  fecha_contrato, id_puesto, salario, 
                                                  comision, id_supervisor, id_departamento, id_empleado))
    
    def delete_empleado(self, id_empleado):
        query = "DELETE FROM EMPLEADOS WHERE ID_EMPLEADO = ?"
        return self.db.execute_non_query(query, (id_empleado,))
    
    # ==================== HISTORICO ====================
    def get_historico(self):
        query = """
        SELECT H.ID_EMPLEADO, E.NOMBRE, E.APELLIDO, H.FECHA_INICIO, H.FECHA_FIN,
               H.ID_PUESTO, P.TITULO_PUESTO, H.ID_DEPARTAMENTO, D.NOMBRE_DEPARTAMENTO
        FROM HISTORICO H
        LEFT JOIN EMPLEADOS E ON H.ID_EMPLEADO = E.ID_EMPLEADO
        LEFT JOIN PUESTOS P ON H.ID_PUESTO = P.ID_PUESTO
        LEFT JOIN DEPARTAMENTOS D ON H.ID_DEPARTAMENTO = D.ID_DEPARTAMENTO
        ORDER BY H.FECHA_INICIO DESC
        """
        return self.db.execute_query(query)
    
    def add_historico(self, id_empleado, fecha_inicio, fecha_fin, id_puesto, id_departamento):
        query = """
        INSERT INTO HISTORICO (ID_EMPLEADO, FECHA_INICIO, FECHA_FIN, ID_PUESTO, ID_DEPARTAMENTO)
        VALUES (?, ?, ?, ?, ?)
        """
        return self.db.execute_non_query(query, (id_empleado, fecha_inicio, fecha_fin, 
                                                  id_puesto, id_departamento))
    
    # ==================== DATOS AUXILIARES ====================
    def get_regiones_list(self):
        """Obtiene lista de regiones para combobox"""
        query = "SELECT ID_REGION, NOMBRE_REGION FROM REGIONES ORDER BY NOMBRE_REGION"
        success, cols, data = self.db.execute_query(query)
        if success:
            return [(row[0], row[1]) for row in data]
        return []
    
    def get_paises_list(self):
        """Obtiene lista de países para combobox"""
        query = "SELECT ID_PAIS, NOMBRE_PAIS FROM PAISES ORDER BY NOMBRE_PAIS"
        success, cols, data = self.db.execute_query(query)
        if success:
            return [(row[0], row[1]) for row in data]
        return []
    
    def get_locaciones_list(self):
        """Obtiene lista de locaciones para combobox"""
        query = "SELECT ID_LOCACION, CIUDAD FROM LOCACIONES ORDER BY CIUDAD"
        success, cols, data = self.db.execute_query(query)
        if success:
            return [(row[0], row[1]) for row in data]
        return []
    
    def get_departamentos_list(self):
        """Obtiene lista de departamentos para combobox"""
        query = "SELECT ID_DEPARTAMENTO, NOMBRE_DEPARTAMENTO FROM DEPARTAMENTOS ORDER BY NOMBRE_DEPARTAMENTO"
        success, cols, data = self.db.execute_query(query)
        if success:
            return [(row[0], row[1]) for row in data]
        return []
    
    def get_puestos_list(self):
        """Obtiene lista de puestos para combobox"""
        query = "SELECT ID_PUESTO, TITULO_PUESTO FROM PUESTOS ORDER BY TITULO_PUESTO"
        success, cols, data = self.db.execute_query(query)
        if success:
            return [(row[0], row[1]) for row in data]
        return []
    
    def get_empleados_list(self):
        """Obtiene lista de empleados para combobox"""
        query = "SELECT ID_EMPLEADO, NOMBRE + ' ' + APELLIDO AS NOMBRE_COMPLETO FROM EMPLEADOS ORDER BY NOMBRE"
        success, cols, data = self.db.execute_query(query)
        if success:
            return [(row[0], row[1]) for row in data]
        return []
