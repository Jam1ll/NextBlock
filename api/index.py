from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from Services.preparing_final_data import getData

app = FastAPI()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# root
@app.get("/api")
def root():
    return {"message": "Backend successfully working on vercel"}


# get all
@app.get("/api/all")
def get_all():
    try:
        data = getData()
        return data
    except Exception as e:
        print(f"Error en /api/all: {e}")
        print(f"Tipo de error: {type(e).__name__}")
        raise HTTPException(status_code=500, detail=f"Error getting data: {str(e)}")
