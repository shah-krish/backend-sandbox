from fastapi import status, HTTPException, Response, APIRouter
from db import find_index, my_posts

router = APIRouter()

# Always use 204 status code for deletes
@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    index = find_index(id)
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Post with ID: {id} was not found")
    else:
        my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)