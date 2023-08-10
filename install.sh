#!/bin/bash

# Actualizar pip
python3 -m pip install --upgrade pip

# Instalar las bibliotecas necesarias
pip3 install pygame numpy numba

# Ejecutar el script de Python
python3 main.py
