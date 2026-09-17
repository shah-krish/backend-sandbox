from fastapi import status, HTTPException, APIRouter
from db import my_posts, find_post

router = APIRouter()

@router.get("/")  # fastAPI instance + http method that the user should use + the path
async def root():
    return {"message": "Hello World"}

@router.get("/posts")
async def get_posts():
    return {"data": my_posts}

@router.get("/posts/{id}")
async def get_post(id: int):  # Always returns string so we make sure we get int
    post = find_post(id)
    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"Message": f"Post with {id} was not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID: {id} was not found")
    return post
