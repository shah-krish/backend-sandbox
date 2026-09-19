from typing import TypedDict, TypeVar

# vertical line means OR. -> to write type hints for a function
# can specify exactly what dictionary will return. here key will be string and value will be str or int or none
# can define it once and reuse
Value = dict[str, str | int | None]
def create_user(name: str, age: int | None = None) -> Value:
    return {"age": age, "name": name}

# In above version, str, int, None applied to all, but with this, only name is str and age is int or None
class Return_Value(TypedDict):
    name: str
    age: int | None
def create_user2(name: str, age: int | None = None) -> Return_Value:
    return  {"age": age, "name": name}

# Generic type hinting
T = TypeVar("T")
# List of anything and we return the same type
def random_choice(items: list[T]) -> T:
    return items[0]


