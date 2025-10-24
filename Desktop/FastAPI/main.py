from fastapi import FastAPI,Path,HTTPException
import json

app = FastAPI()

def load_data():
    with open("patient.json","r") as f:
        data = json.load(f)

    return data


@app.get("/")
def hello():
    return {"message":"hello Patient Managemnet Syestem API"}

@app.get("/about")
def about():
    return{"message":"A fully Functional API to manage your patient records"}

@app.get("/view")
def view():
    data = load_data()

    return data



