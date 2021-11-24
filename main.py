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
def func1():
	return data

@app.get("/{random1}")
def return_data(random1: str):
	for i in data:
		if i['name'] == random1:
			return i
		else:
			return "Not Found"
