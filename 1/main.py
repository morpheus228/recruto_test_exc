from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def read_root(name: str, message: str):
    return f"Hello {name}! {message}!"