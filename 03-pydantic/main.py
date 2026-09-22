from datetime import datetime, UTC
from pydantic import BaseModel, ValidationError, Field, EmailStr, HttpUrl, SecretStr
from typing import Literal, Annotated
from uuid import UUID, uuid4


class User(BaseModel):
    uid: Annotated[int, Field(gt=0)] # can only be greater than 0
    username: Annotated [str, Field(min_length=3, max_length=20)] # length restrictions
    email: str

    age: Annotated[int, Field(ge=13, le=130)] # greater equals and less equals
    verified_at: datetime | None = None

    bio: str = "" # default value blank
    is_active: bool = True
    full_name: str | None = None # makes it optional

class blogPost(BaseModel):
    title: str
    content: Annotated[str, Field(min_length= 10)]
    view_count: int = 0
    is_published: bool = False

    # Field(default_factory) creates a new instance everytime. if [] used, same will be referenced everytime
    tags: list[str] = Field(default_factory=list)

    # lambda = use when needed so each models gets a fresh timestamp
    create_at: datetime = Field(default_factory=lambda: datetime.now(tz=UTC))

    author_id: str | int

    # status can only be one of these 3 strings
    status = Literal["archived", "draft", "published"] = "draft"

    # regular expression
    slug: Annotated[str, Field(pattern=r"^[a-z0-9]$")]


