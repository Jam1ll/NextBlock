import sys
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Services.preparing_final_data import getData

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api")
def api_root():
    return {"message": "Backend funcionando correctamente en Vercel"}


@app.get("/api/all")
def get_all():
    try:
        data = getData()
        return data
    except Exception as e:
        print(f"Error en /api/all: {e}")
        print(f"Tipo de error: {type(e).__name__}")
        raise HTTPException(
            status_code=500, detail=f"Error al obtener los datos: {str(e)}"
        )
