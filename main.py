from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from api.models import Vacancy
from api.database import vacancies, create_db_and_tables
import os

app = FastAPI()

# Дозволяємо запити з будь-якого джерела (для карти)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Створюємо базу при запуску
@app.on_event("startup")
def startup():
    create_db_and_tables()

# Отримати всі активні вакансії
@app.get("/vacancies")
def get_vacancies():
    active = [v for v in vacancies if v["is_active"]]
    return JSONResponse(content=active)

# Віддати HTML-карту
@app.get("/map")
def get_map():
    return FileResponse(os.path.join("map", "index.html"))

