# Usar imagen base oficial de Python
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /hola

# Copiar archivo de dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de la aplicación
COPY hola.py .

# Exponer el puerto
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "hola.py"]