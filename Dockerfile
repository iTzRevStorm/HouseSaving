# Usamos una imagen base de Python ligera
FROM python:3.11-slim

# Establecemos el directorio de trabajo
WORKDIR /app

# Instalamos las dependencias
RUN pip install fastapi uvicorn python-multipart oracledb

# ----- CAMBIO IMPORTANTE -----
# 1. Copiamos la carpeta de la Wallet al contenedor
# (Asegúrate de que 'Wallet_housesavingdb' sea el nombre de tu carpeta)
COPY Wallet_housesavingdb /app/Wallet_housesavingdb

# 2. Le decimos a Oracle dónde encontrar la Wallet
ENV TNS_ADMIN=/app/Wallet_housesavingdb
# ---------------------------

# Copiamos sus archivos (main.py y consumo.py)
COPY main.py .
COPY consumo.py .

# Comando que inicia el servidor Uvicorn dentro del contenedor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]