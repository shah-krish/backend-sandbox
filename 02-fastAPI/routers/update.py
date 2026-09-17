from fastapi import HTTPException, status, APIRouter
from db import Post, find_index, my_posts

router = APIRouter()

@router.put("/posts/{id}")
async def update_post(id: int, post: Post):
    index = find_index(id)
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID: {id} was not found")
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"Data": post_dict}
