@echo off
title CRUD SOF108 - Sistema de Gestion de Empleados
color 0A

echo ========================================
echo   CRUD SOF108
echo   Sistema de Gestion de Empleados
echo ========================================
echo.

REM Verificar si Python esta instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no esta instalado o no esta en el PATH
    echo.
    echo Descargar Python desde: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo [OK] Python encontrado
echo.

REM Verificar si las dependencias estan instaladas
echo Verificando dependencias...
python -c "import pyodbc, customtkinter" >nul 2>&1
if errorlevel 1 (
    echo [AVISO] Instalando dependencias...
    echo.
    pip install -r requirements.txt
    if errorlevel 1 (
        echo [ERROR] No se pudieron instalar las dependencias
        pause
        exit /b 1
    )
    echo.
    echo [OK] Dependencias instaladas
    echo.
)

echo [OK] Dependencias verificadas
echo.
echo Iniciando aplicacion...
echo.

REM Ejecutar la aplicacion
python main.py

if errorlevel 1 (
    echo.
    echo [ERROR] La aplicacion termino con errores
    pause
)
