from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Список для збереження імен
names = []

# Схема для отримання даних від користувача
class NameRequest(BaseModel):
    name: str

@app.post("/add-name")
async def add_name(request: NameRequest):
    """Додає нове ім'я до списку."""
    if request.name in names:
        raise HTTPException(status_code=400, detail="Ім'я вже існує в списку.")
    names.append(request.name)
    return {"message": "Ім'я успішно додано.", "names": names}

@app.get("/get-names")
async def get_names():
    """Повертає всі збережені імена."""
    return {"names": names}

@app.delete("/delete-name/{name}")
async def delete_name(name: str):
    """Видаляє ім'я зі списку."""
    if name not in names:
        raise HTTPException(status_code=404, detail="Ім'я не знайдено у списку.")
    names.remove(name)
    return {"message": "Ім'я успішно видалено.", "names": names}

# Обробка помилок для дублювання або відсутності імен
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc: HTTPException):
    return {"error": exc.detail}
