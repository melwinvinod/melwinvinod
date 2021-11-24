from fastapi import FastAPI
import json

app =  FastAPI()
data=[{
  "name": "Elon Musk",
  "email": "elon@spacex.com",
  "image": "link to image"
},
{
  "name": "Jeff Bezos",
  "email": "jeff@blueorigin.com",
  "image": "link to image"
}]

@app.get("/")
def func1():
	return data

@app.get("/{random1}")
def return_data(random1: str):
	for i in data:
		if i['name'] == random1:
			return "Happy Birthday,"+i['name']+"!"
		else:
			return "Not Found"
