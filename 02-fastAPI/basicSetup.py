from typing import Optional
from random import randrange
from fastapi import FastAPI, status, HTTPException, Response
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()  # fastAPI instance created


class Post(BaseModel):
    title: str
    content: str
    published: bool = True  # If the user doesn't provide a value, it returns true instead of an error
    rating: Optional[int] = None  # Defaults to null if no value provided


my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "title of post 2", "content": "content of post 2", "id": 2}]


def find_post(id):
    for post in my_posts:
        if id == post['id']:
            return post

def find_index(id):
    for i, post in enumerate(my_posts):
        if id == post['id']:
            return i
    return None

@app.get("/")  # fastAPI instance + http method that the user should use + the path
async def root():
    return {"message": "Hello World"}


@app.get("/posts")
async def get_posts():
    return {"data": my_posts}


@app.post("/createposts", status_code=status.HTTP_201_CREATED)
# Use the pydantic Post class to make sure we get data exactly how we wanted
async def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 100000000)  # dont have db rn, so handling id manually
    my_posts.append(post_dict)
    return {"data": post_dict}


@app.get("/posts/{id}")
async def get_post(id: int):  # Always returns string so we make sure we get int
    post = find_post(id)
    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"Message": f"Post with {id} was not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID: {id} was not found")
    return post


# Always use 204 status code for deletes
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    index = find_index(id)
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Post with ID: {id} was not found")
    else:
        my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
async def update_post(id: int, post: Post):
    index = find_index(id)
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID: {id} was not found")
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"Data": post_dict}
