import os
import csv
import shutil
from tempfile import NamedTemporaryFile
from .templates import render_context_plain

filename = os.path.join(os.getcwd(), "data.csv")
fieldnames = ['id', 'name', 'email']

def gen_seed_data():
	with open(filename, "w+") as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		writer.writerow({"id":0, "name": "Barry Allen", "email": "barrallen@gmail.com"})
		writer.writerow({"id":1, "name": "Joe West", "email": "joewest@gmail.com"})
		writer.writerow({"id":2, "name": "Iris West", "email": "iriswest@gmail.com"})
		writer.writerow({"id":3, "name": "Wally West", "email": "wallywest@gmail.com"})
		writer.writerow({"id":4, "name": "Oliver Queen", "email": "oliverqueen@gmail.com"})
		writer.writerow({"id":5, "name": "John Diggle", "email": "johndiggle@gmail.com"})
		writer.writerow({"id":6, "name": "Matthew Murdock", "email": "mattewmurdock@gmail.com"})
		writer.writerow({"id":7, "name": "Karen Page", "email": "karenpage@gmail.com"})
		writer.writerow({"id":8, "name": "Luke Cage", "email": "lukecage@gmail.com"})

def read_data(user_id = None):
	with open(filename, "r") as csvfile:
		reader = csv.DictReader(csvfile, fieldnames=fieldnames)
		user = None

		# skip the header
		next(reader)
		
		for row in reader:
			if user_id is not None and int(row.get("id")) == user_id:
				user = row
				break

		if user is not None:
			print(user)
		else:
			print("{id} is not valid user id".format(id=user_id))

def send_email(user_id):
	with open(filename, "r") as csvfile:
		reader = csv.DictReader(csvfile, fieldnames=fieldnames)

		# skip the header
		next(reader)

		for row in reader:
			if row.get("id") != None and int(row["id"]) == user_id:
				print(render_context_plain(row))
				break


