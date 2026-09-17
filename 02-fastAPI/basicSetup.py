from fastapi import FastAPI
from routers import read, create, update, delete

app = FastAPI()  # fastAPI instance created

app.include_router(read.router)
app.include_router(create.router)
app.include_router(update.router)
app.include_router(delete.router)

