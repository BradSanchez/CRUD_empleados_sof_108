"""
Script de verificación de instalación
Ejecutar este script para verificar que todas las dependencias están instaladas correctamente
"""

import sys

def test_python_version():
    """Verifica la versión de Python"""
    print("🔍 Verificando versión de Python...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"   ✅ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"   ❌ Python {version.major}.{version.minor}.{version.micro} - Se requiere Python 3.8+")
        return False

def test_module(module_name, display_name=None):
    """Verifica si un módulo está instalado"""
    if display_name is None:
        display_name = module_name
    
    print(f"🔍 Verificando {display_name}...")
    try:
        __import__(module_name)
        print(f"   ✅ {display_name} - OK")
        return True
    except ImportError:
        print(f"   ❌ {display_name} - NO INSTALADO")
        print(f"      Instalar con: pip install {module_name}")
        return False

def test_pyodbc_drivers():
    """Verifica los drivers ODBC disponibles"""
    print("🔍 Verificando drivers ODBC...")
    try:
        import pyodbc
        drivers = pyodbc.drivers()
        if drivers:
            print(f"   ✅ Drivers encontrados: {len(drivers)}")
            for driver in drivers:
                if "SQL Server" in driver:
                    print(f"      • {driver}")
            return True
        else:
            print("   ⚠️  No se encontraron drivers ODBC")
            print("      Instalar ODBC Driver 17 for SQL Server")
            return False
    except Exception as e:
        print(f"   ❌ Error al verificar drivers: {e}")
        return False

def main():
    """Función principal"""
    print("=" * 60)
    print("🚀 VERIFICACIÓN DE INSTALACIÓN - CRUD SOF108")
    print("=" * 60)
    print()
    
    results = []
    
    # Verificar Python
    results.append(test_python_version())
    print()
    
    # Verificar módulos
    results.append(test_module("pyodbc", "pyodbc (Conexión SQL Server)"))
    print()
    
    results.append(test_module("customtkinter", "CustomTkinter (Interfaz gráfica)"))
    print()
    
    results.append(test_module("PIL", "Pillow (Procesamiento de imágenes)"))
    print()
    
    results.append(test_module("tkcalendar", "tkcalendar (Selector de fechas)"))
    print()
    
    # Verificar drivers ODBC
    results.append(test_pyodbc_drivers())
    print()
    
    # Resumen
    print("=" * 60)
    if all(results):
        print("✅ TODAS LAS VERIFICACIONES PASARON")
        print("🎉 La aplicación está lista para ejecutarse")
        print()
        print("Ejecutar la aplicación con:")
        print("   python main.py")
    else:
        print("❌ ALGUNAS VERIFICACIONES FALLARON")
        print("⚠️  Instalar las dependencias faltantes antes de ejecutar")
        print()
        print("Instalar todas las dependencias con:")
        print("   pip install -r requirements.txt")
    print("=" * 60)

if __name__ == "__main__":
    main()
