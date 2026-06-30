from fastapi import FastAPI
from app.routes.livros import router as livros_router

app = FastAPI()
app.include_router(livros_router)





