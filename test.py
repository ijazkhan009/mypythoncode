from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running"}

@app.get("/test")
def test():
    return {"message": "test connection passed"}

@app.get("/hello")
def hello(name: str = "world"):
    return {"message": f"hello {name}"}