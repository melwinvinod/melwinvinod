from fastapi import FastAPI
import json

app =  FastAPI()
data=[{
  "name": "Elon Musk",
  "email": "melwin96@yahoo.com",
  "image": "https://funkylife.in/wp-content/uploads/2021/10/happy-birthday-wishes-1.jpg"
},
{
  "name": "Jeff Bezos",
  "email": "sanjayamazed@gmail.com",
  "image": "https://funkylife.in/wp-content/uploads/2021/10/happy-birthday-wishes-1.jpg"
}]

@app.get("/")
def root():
    return data

@app.get("/{name}")
def return_data_based_on_name(name: str):
    for i in data:
        if i['name']==name:
            return i
