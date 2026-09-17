from typing import Optional
from pydantic import BaseModel


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
