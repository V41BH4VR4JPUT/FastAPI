from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Car(BaseModel):
    Company : str
    model : str
    year : int

cars : List[Car] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the Car API"}

@app.get("/cars")
def get_cars():
    return cars

@app.post("/cars")
def add_car(car: Car):
    cars.append(car)
    return {"message": "Car added successfully", "car": car}

@app.put("/cars/{car_index}")
def update_car(car_index: int, car: Car):
    if 0 <= car_index < len(cars):
        cars[car_index] = car
        return {"message": "Car updated successfully", "car": car}
    else:
        return {"error": "Car index out of range"}, 404
    
@app.delete("/cars/{car_index}")
def delete_car(car_index: int):
    if 0 <= car_index < len(cars):
        removed_car = cars.pop(car_index)
        return {"message": "Car deleted successfully", "car": removed_car}
    else:
        return {"error": "Car index out of range"}, 404