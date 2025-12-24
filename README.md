# NextBlock

**NextBlock** es una plataforma inteligente para el análisis, predicción y recomendación de inversiones inmobiliarias. Utiliza modelos de Machine Learning para clasificar propiedades y visualizarlas en un dashboard interactivo junto a un chatbot integrado.

## Visión General

El proyecto consta de dos partes principales:

1. **Backend (Python/FastAPI):** Procesa datos masivos, aplica IA (`RandomForest`) para predecir el potencial de inversión y expone una API REST.
2. **Frontend (React):** Consume la API para visualizar las propiedades en un mapa interactivo codificado por colores según su rentabilidad.

---

## Stack Tecnológico

| Área             | Tecnologías Clave                                                   |
| :--------------- | :------------------------------------------------------------------ |
| **Frontend**     | React (Vite), TailwindCSS + DaisyUI, React Leaflet, Recharts, Axios |
| **Backend**      | Python 3.x, FastAPI, Uvicorn                                        |
| **Data Science** | Pandas, NumPy, Scikit-learn, pgeocode                               |

---

## Inicio Rápido

Para ejecutar la aplicación completa, necesitarás dos terminales abiertas: una para el backend y otra para el frontend.

### 1. Configuración del Backend (Puerto 8000)

El backend procesa los datos y sirve la API en vercel

```bash
# 1. Navegar al directorio raíz (donde está main.py)
# 2. Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate  # Mac/Linux
.\venv\Scripts\activate   # Windows

# 3. Instalar dependencias
pip install fastapi uvicorn pandas numpy scikit-learn pgeocode

# 4. Levantar el servidor
uvicorn main:app --reload
```

### 2. Configuración del Frontend

El frontend se conecta al backend local para obtener los datos.

```bash
# 1. Navegar al directorio frontend
cd frontend

# 2. Instalar dependencias
npm install

# 3. Ejecutar la aplicación
npm run dev
```

---

## Arquitectura y Flujo de Datos

### Flujo de Backend (AI & Data)

- Ingesta: Se procesan datos históricos desde CSV (texas_master_data.csv).
- IA: RealEstateSmartPredictor.py clasifica las zonas (Barata-Alto Potencial, Estable, Sobrevalorada).
- Geo: Se enriquecen los datos con Latitud/Longitud.
- API: FastAPI sirve el resultado final en formato JSON.

### Integración Frontend

- Fuente de Datos: Consume GET /api/all del backend.
- Mapa Interactivo:
  - 🟢: Alto Potencial.
  - 🟡: Estable.
  - 🔴: Bajo Potencial.
