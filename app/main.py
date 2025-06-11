from fastapi import FastAPI
from user.interface.controller.user_controller import router as user_router

user_service = UserService()

app = FastAPI()

app.include_router(user_router)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}