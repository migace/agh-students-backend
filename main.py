from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def test():
    return {"Hello": "World"}


@app.get("/items/{item_id}/{category}")
def read_item(item_id: int, category: str, q: Union[str, None] = None):
    return {"item_id": item_id, "category": category, "q": q}


@app.get("/students")
def get_students():
    return {
        "students": [
            {
                "name": "John",
                "surname": "Doe #1",
                "age": 17,
                "email": "test@example.com"
            },
            {
                "name": "John",
                "surname": "Doe #2",
                "age": 17,
                "email": "test@example.com"
            },
            {
                "name": "John",
                "surname": "Doe #3",
                "age": 17,
                "email": "test@example.com"
            },
            {
                "name": "John",
                "surname": "Doe #4",
                "age": 17,
                "email": "test@example.com"
            }
        ]
    }
