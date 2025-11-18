from fastapi import FastAPI
import uvicorn

from calculations.addition import add_numbers


app = FastAPI()


@app.get("/add")
def add(a: int, b: int):
    return {"result": add_numbers(a, b)}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
 