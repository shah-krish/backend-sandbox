from typing import Optional

from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()  # fastAPI instance created

class Post(BaseModel):
    title: str
    content: str
    published: bool = True # If the user doesn't provide a value, it returns true instead of an error
    rating: Optional[int] = None # Defaults to null if no value provided

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": "1"},
            {"title": "title of post 2", "content": "content of post 2", "id": "2"}]
@app.get("/")  # fastAPI instance + http method that the user should use + the path
async def root():
    return {"message": "Hello World"}


@app.get("/posts")
async def get_posts():
    return {"data": my_posts}


@app.post("/createposts")
# Use the pydantic Post class to make sure we get data exactly how we wanted
async def create_posts(post: Post):
    print(post)
    print(post.dict()) # Can covert easily to dictionary
    return {"data": post}
