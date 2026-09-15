from typing import Optional
from random import randrange
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()  # fastAPI instance created

class Post(BaseModel):
    title: str
    content: str
    published: bool = True # If the user doesn't provide a value, it returns true instead of an error
    rating: Optional[int] = None # Defaults to null if no value provided

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "title of post 2", "content": "content of post 2", "id": 2}]

def find_post(id):
    for post in my_posts:
        if id == post['id']:
            return post
    return None

@app.get("/")  # fastAPI instance + http method that the user should use + the path
async def root():
    return {"message": "Hello World"}


@app.get("/posts")
async def get_posts():
    return {"data": my_posts}

@app.post("/createposts")
# Use the pydantic Post class to make sure we get data exactly how we wanted
async def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 100000000) # dont have db rn, so handling id manually
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}")
async def get_post(id: int): # Always returns string so we make sure we get int
    post = find_post(id)
    if post is None:
        return {"Error": "Wrong ID"}
    return post

