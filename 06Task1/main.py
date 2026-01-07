from fastapi import FastAPI
from routes import router

app = FastAPI(title="Gym Management System")

app.include_router(router)


@app.get("/")      #Path Defining 
def root():
    return {"message": "Gym Management System API is running"}
