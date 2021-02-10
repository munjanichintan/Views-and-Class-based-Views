import requests
import json

# URL = "http://localhost:8000/stuinfo/"
URL = "http://localhost:8000/stuinfo/"

def get_data(id=None):
	data = {}
	if id is not None:
		data = {'id': id}
	headers = {'content-Type': 'application/json'}
	json_data = json.dumps(data)
	r = requests.get(url=URL, headers=headers, data=json_data)
	data = r.json()
	print(data)

# get_data()

def post_data():
	data = {
	   'name': 'Jack',
	   'roll': 10,
	   'city': 'New York'
	}
	headers = {'content-Type': 'application/json'}
	json_data = json.dumps(data)
	r = requests.post(url=URL, headers=headers, data=json_data)
	data = r.json()
	print(data)

# post_data()

def update_data():
	data = {
	   'id': 4,
	   'name': 'Abhishek',
	   'roll': 40,
	   'city': 'Jamnagar'
	}
	headers = {'content-Type': 'application/json'}
	json_data = json.dumps(data)
	r = requests.put(url=URL, headers=headers, data=json_data)
	data = r.json()
	print(data)

# update_data()

def delete_data():
	data = {'id': 4}
	headers = {'content-Type': 'application/json'}
	json_data = json.dumps(data)
	r = requests.delete(url=URL, headers=headers, data=json_data)
	data = r.json()
	print(data)

# delete_data()