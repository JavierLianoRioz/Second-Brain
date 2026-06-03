#!/bin/bash

# Script para sincronizar archivos marcados como 'private: true' con .gitignore
# Mantenido por Gemini CLI

GITIGNORE=".gitignore"
START_MARKER="### PRIVATE-FILES-START ###"
END_MARKER="### PRIVATE-FILES-END ###"

# Asegurar que el archivo .gitignore existe
touch "$GITIGNORE"

# Crear marcadores si no existen
if ! grep -q "$START_MARKER" "$GITIGNORE"; then
    echo -e "\n$START_MARKER\n$END_MARKER" >> "$GITIGNORE"
fi

# Encontrar archivos con 'private: true' en el frontmatter
PRIVATE_FILES=$(grep -rlE "^\s*private:\s*true" --include="*.md" . | sed 's|^\./||')

# Construir el nuevo bloque de archivos privados
TEMP_FILE=$(mktemp)

# Copiar todo lo anterior al marcador de inicio
sed -n "1,/$START_MARKER/p" "$GITIGNORE" > "$TEMP_FILE"

# Añadir los archivos encontrados
if [ -n "$PRIVATE_FILES" ]; then
    echo "$PRIVATE_FILES" >> "$TEMP_FILE"
fi

# Añadir el marcador de fin y todo lo posterior
sed -n "/$END_MARKER/,\$p" "$GITIGNORE" >> "$TEMP_FILE"

# Reemplazar el .gitignore original
mv "$TEMP_FILE" "$GITIGNORE"

# Opcional: Remover de la caché de git si ya estaban trackeados
if [ -n "$PRIVATE_FILES" ]; then
    echo "$PRIVATE_FILES" | while read -r file; do
        git rm --cached "$file" 2>/dev/null
    done
fi

echo "Sincronización de privacidad completada."
