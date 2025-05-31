from pydantic import BaseModel # type: ignore
from datetime import datetime

class User(BaseModel):
    id: int
    name : str = "Vaibhav"
    signup_ts : datetime | None = None
    friends: list[int] = []

external_data = {
    "id": "123",
    "signup_ts": "2023-10-01T12:00:00",
    "friends": [1, 2, 3]
}
user = User(**external_data)
print(user)
print(user.id)