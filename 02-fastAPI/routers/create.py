from fastapi import APIRouter
from random import randrange
from fastapi import status
from db import my_posts, Post

router = APIRouter()

@router.post("/createposts", status_code=status.HTTP_201_CREATED)
# Use the pydantic Post class to make sure we get data exactly how we wanted
async def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 100000000)  # dont have db rn, so handling id manually
    my_posts.append(post_dict)
    return {"data": post_dict}

