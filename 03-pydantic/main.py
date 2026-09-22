from datetime import datetime
from pydantic import BaseModel, ValidationError

class User(BaseModel):
    uid: int
    username: str
    email: str

    verified_at: datetime | None = None

    bio: str = "" # default value blank
    is_active: bool = True
    full_name: str | None = None # makes it optional

try:
    u1 = User(
        uid = 123,
        username = None,
        email = "krish@test.com"
    )
except ValidationError as e:
    print(e)

u1.bio = "Python developer"
print(u1.model_dump()) # Convert to python dictionary
print(u1.model_dump_json(indent=2)) # Convert to json string


