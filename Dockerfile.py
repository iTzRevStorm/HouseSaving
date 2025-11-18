# Usamos una imagen base de Python ligera
FROM python:3.11-slim

# Establecemos el directorio de trabajo
WORKDIR /app

# Instalamos las dependencias
# AÑADIMOS 'oracledb' para conectar a la base de datos Oracle
RUN pip install fastapi uvicorn python-multipart oracledb

# Creamos un archivo de requisitos (buena práctica)
# RUN echo "fastapi" >> requirements.txt
# RUN echo "uvicorn" >> requirements.txt
# RUN echo "python-multipart" >> requirements.txt
# RUN echo "oracledb" >> requirements.txt
# RUN pip install -r requirements.txt

# Copiamos sus archivos (main.py y consumo.py)
COPY main.py .
COPY consumo.py .

# Comando que inicia el servidor Uvicorn dentro del contenedor
# Render usará este comando.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]