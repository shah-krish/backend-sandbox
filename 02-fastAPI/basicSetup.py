from fastapi import FastAPI

app = FastAPI() #fastAPI instance created

@app.get("/") #fastAPI instance + http method that the user should use + the path
async def root():
    return {"message": "Hello World"}