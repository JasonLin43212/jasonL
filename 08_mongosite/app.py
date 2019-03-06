#Lingo -- Kevin Lin and Jason Lin
#SoftDev1 pd07
#K08 -- Ay Mon, Go Git It From Yer Flask
#2019-03-06

from flask import Flask, render_template, request
from pymongo import MongoClient
import json
app = Flask(__name__) # instantiates an instance of Flask


SERVER_ADDR = "142.93.57.60" # Jason's droplet
#SERVER_ADDR = "68.183.104.137" # Kevin's droplet
connection = MongoClient(SERVER_ADDR)
db = connection.Lingo
collection = db.prizes
prizeDct = None

@app.route("/") #Linking a function to a route
def home():
    return render_template("nobel.html")

if __name__ == "__main__":
    app.debug = True
    app.run()


with open("prize.json") as dct:
    collection.drop()
    prizeDct = json.load(dct)

def importJson():
    collection.insert_many(prizeDct["prizes"])

def search_year(year):
    # Gets all of the documents with the given year
    # collection is the same thing as db.prizes
    print("Prizes with year:",year)
    prizes = collection.find({"year":str(year)})
    for prize in prizes:
        print(prize,"\n")

def search_category(category):
    # Gets all of the documents with the given category
    print("Prizes with category:",category)
    category = category.lower()
    prizes = collection.find({"category":category})
    for prize in prizes:
        print(prize,"\n")

def search_category_year(category,year):
    # Gets all of the documents with the given category and year
    print("Prizes from:",year,"with category:",category)
    category = category.lower()
    prizes = collection.find({'$and': [{"category":category},{"year":str(year)}]})
    for prize in prizes:
        print(prize,"\n")

def search_category_after_year(category,year):
    # Gets all of the documents with the given category and is after the given year
    print("Prizes after",year,"with category:",category)
    category = category.lower()
    prizes = collection.find({"$and":[{"category":category},{"year":{"$gte":str(year)}}]})
    for prize in prizes:
        print(prize)

def search_num_lauretes(num):
    # Gets all of the documents where the number of lauretes is that number
    print("Prizes that had",num,"lauretes")
    prizes = collection.find()
    output = []
    for prize in prizes:
        if len(prize['laureates']) == num:
            output.append(prize)
    for prize in output:
        print(prize)
