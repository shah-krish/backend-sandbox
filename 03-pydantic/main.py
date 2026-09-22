from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    age: int
# Throws errors for email and age
u1 = User(username = "Krish", email=5, age="5")
