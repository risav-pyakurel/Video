from fastapi import FastAPI

# from config import Settings

app = FastAPI()


@app.get("/")
def homepage():
    return {"hello" : "world", "keyspace":"Sudarshan"} # going to be a json data for REST API server
    