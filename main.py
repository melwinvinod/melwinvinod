from fastapi import FastAPI
import json
from jsonpath_ng import jsonpath, parse

app =  FastAPI()
data=[
	{
		"random": 74,
		"firstname": "Rayna",
		"lastname": "Standing"
	},
	{
		"random": 64,
		"firstname": "Karolina",
		"lastname": "Lauraine"
	},
	{
		"random": 6,
		"firstname": "Joeann",
		"lastname": "Ingra"
	},
	{
		"random": 3,
		"firstname": "Jemie",
		"lastname": "Carey"
	}
]

@app.get("/")
def func1():
	return data

@app.get("/{random1}")
def return_anme(random1: int):
	json_data = json.loads(data)
	jsonpath_expr = parse('data[*]')
	return jsonpath_expr
