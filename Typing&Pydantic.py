# Typing modules

def greet(name: str, age: int) -> str:
   return (f"Hello, my name is {name} and my age is: {age}")

print(greet("Dipin", 21))


from typing import Literal

def set_mode(mode: Literal["auto", "manual"]) -> None:
    print(f"Mode set to {mode}")

set_mode("auto")  # Valid


from typing import Any

def func(x: Any) -> None:
    print("x will be of any type.")


from typing import Union

def func(x: Union[int, str]) -> Union[int, str]:

    if(x == "45"):
        return f"{x} is a integer."
    return x

# Pydantic

# Pydantic is a python library that helps us in defining and validating data models easily.
# Pydantic is the concept of models. A pydanic model in a python class that inherits from BaseModel and is used to define the structure, validation and parsing logic for our data

from pydantic import BaseModel

class UserProfile(BaseModel):
    name: str
    age: int
    email: str

user = UserProfile(name = "Dipin", age = 20, email = "xyz@gmail.com")
print(user)

print(user.name)
user.age = 21
print(user.email)

# Default Values

class UserProfile(BaseModel):
    name: str
    age: int = 25
    email: str
    is_active: bool = True

user = UserProfile(name = "Dipin", email = "xyz.14@gmail.com")
print(user)

# Convert model instance to Dict

class User(BaseModel):
    id: int
    name: str

user = User(id = 123, name = "Rey")
print(user.dict())

from pydantic import field_validator

class User(BaseModel):
    age: int
    name: str

    @field_validator("age")
    def func(cls, value):
        if(value < 18):
            raise ValueError("Age must be 18")
        return value
    
user = User(name = "Dipin", age = 21)