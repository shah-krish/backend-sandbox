from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()  # fastAPI instance created


@app.get("/")  # fastAPI instance + http method that the user should use + the path
async def root():
    return {"message": "Hello World"}


@app.get("/posts")
async def get_posts():
    return {"data": "This is your posts"}


@app.post("/createposts")
# Extract everything from body (...) and store it in a python dictionary called payload
async def create_posts(payLoad: dict = Body(...)):
    print(payLoad)
    return {"new_post": f"title = {payLoad['title']}, content = {payLoad['content']}"}
