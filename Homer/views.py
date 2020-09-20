from Homer import app#, db
# from scraper.py import scrape
from flask import render_template, request, redirect
# from Homer.models import Fact

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods = ["GET", "POST"])
def results():
    # scrape()
    naturalDisastors = ["list", "here"]
    wasteLocation = "amani"
    AQI = "was"
    carbonPPM = "here"
    zipcode = request.forms.get('zip')
    return render_template("results.html", data={"zip":zipcode, "natDis":naturalDisastors, "waste":wasteLocation, "AQI":AQI, "carbon":carbonPPM})
