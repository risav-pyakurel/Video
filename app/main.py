from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def homepage():
    return {"hello" : "world"} # going to be a json data for REST API server
    