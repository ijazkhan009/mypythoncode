from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
def home():
    print("hellooworlds")
    return {"message": "APII is running"}

@app.get("/test")
def test():
    return {"message": "test connection passed"}

@app.get("/hello")
def hello(name: str = "world"):
    return {"message": f"hello {name}"}