# main.py - API con FastAPI y Tarea de Fondo (Background Task)
from fastapi import FastAPI
import asyncio
from consumo import (
    init_db,  # Cambiado desde crear_tablas
    guardar_consumo_energia,
    obtener_datos_recientes,
    generar_consumo_energia
)
from datetime import datetime
import time

# ==================================
# TAREA DE SIMULACIÓN EN SEGUNDO PLANO
# ==================================
async def simular_consumo_automatico():
    """Bucle infinito que genera y guarda datos de energía cada 5 segundos."""
    print("Iniciando simulación automática de ENERGÍA...")
    while True:
        try:
            # 1. Generar el dato
            kwh = generar_consumo_energia()

            # 2. Guardar en la base de datos
            guardar_consumo_energia(kwh)

            hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{hora}] GENERADO: Energía={kwh:.4f}kWh")
        
        except Exception as e:
            print(f"Error en la simulación de datos: {e}")
        
        # Espera 5 segundos
        await asyncio.sleep(5) 

# ==================================
# APLICACIÓN FASTAPI
# ==================================
app = FastAPI(title="API HouseSaving Electricidad")

@app.on_event("startup")
async def startup_event():
    init_db()  # Llama a la nueva función de inicialización de Oracle
    asyncio.create_task(simular_consumo_automatico())
    print("API lista. Tarea de simulación iniciada.")


@app.get("/")
def inicio():
    """Mensaje de bienvenida y estado de la API."""
    return {"mensaje": "API de Consumo de Energía funcionando. Los datos se generan automáticamente en segundo plano."}

@app.get("/ultimos/")
def ultimos_datos():
    """Endpoint para que Flutter lea los 5 registros más recientes."""
    datos = obtener_datos_recientes()
    return {"ultimos_registros": datos}