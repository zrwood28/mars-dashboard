from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri = "mongodb://localhost:27017/mars_app")

@app.route("/")
def home():

    mars_dict = mongo.db.mars_dict.find_one()

    return render_template("index.html", mars_dict = mars_dict)

@app.route("/scrape")
def scraper():

    mars_dict = mongo.db.mars_dict

    mars_dict_data = scrape_mars.scrape()

    mars_dict.update_one({}, {"$set": mars_dict_data}, upsert = True)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)
