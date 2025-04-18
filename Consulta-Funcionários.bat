@echo off
echo ===================================
echo Iniciando Sistema de Consulta
echo ===================================
echo.
echo Verificando bibliotecas necessarias...
pip install pandas openpyxl --quiet
cls
echo ===================================
echo Sistema de Consulta de Motoristas
echo ===================================
echo.
python leitor_planilha.py
echo.
echo ===================================
echo Programa finalizado
echo ===================================
pause > nul