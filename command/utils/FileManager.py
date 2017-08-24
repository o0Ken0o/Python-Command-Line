import os
import csv
import shutil
from tempfile import NamedTemporaryFile

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

def read_data():
	with open(filename, "r") as csvfile:
		reader = csv.DictReader(csvfile, fieldnames=fieldnames)
		for row in reader:
			print(row)


