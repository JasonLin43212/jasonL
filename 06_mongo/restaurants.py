'''
Blinking Retina -- Tina Wong - Jason Lin
SoftDev2 pd7
K06 -- Yummy Mongo Py
2019-02-28
'''
import pymongo
#SERVER_ADDR = "142.93.6.251" # Tina's droplet
#SERVER_ADDR = "142.93.57.60" # Jason's droplet
connection = pymongo.MongoClient(SERVER_ADDR)
db = connection.test
collection = db.restaurants

def search_borough(borough):
	restaurants = db.restaurants.find({"borough": borough})
	for restaurant in restaurants:
		print(restaurant)
# search_borough("Brooklyn")

def search_zipcode(zipcode):
	restaurants = db.restaurants.find({"address.zipcode": str(zipcode)})
	for restaurant in restaurants:
		print(restaurant)
# search_zipcode(11229)

def search_zipcode_grade(zipcode, grade):
	restaurants = db.restaurants.find({'$and': [{"address.zipcode": str(zipcode)},{"grades.0.grade": grade}]})
	for restaurant in restaurants:
		print(restaurant)
# search_zipcode_grade(11229, "A")

def search_threshold(zipcode, score):
	restaurants = db.restaurants.find({'$and': [{"address.zipcode": str(zipcode)},{"grades.0.score":{ '$lt': score }}]});
	for restaurant in restaurants:
		print(restaurant)
# search_threshold(11229, 10)

def search_name_cuisine(name, cuisine):
	restaurants = db.restaurants.find({'$or': [{"name": name},{"cuisine": cuisine}]})
	for restaurant in restaurants:
		print(restaurant)
# search_name_cuisine("Dunkin Donuts", "Chinese")
