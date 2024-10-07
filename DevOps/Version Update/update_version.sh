#!/bin/bash

# Definir el nuevo valor de la versión
NUEVA_VERSION="v1.5.3"

# Usar sed para reemplazar el valor de la versión en el archivo setup.py
sed -i "s/version=\"[^\"]*\"/version=\"$NUEVA_VERSION\"/" setup.py

echo "Versión actualizada a $NUEVA_VERSION en setup.py"
