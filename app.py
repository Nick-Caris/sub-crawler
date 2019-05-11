from flask import Flask, jsonify
from sub_crawler.__main__ import crawl
import datetime

app = Flask(__name__)


@app.route("/subs")
def subs():
    return jsonify(crawl(get_week_nr()))


def get_week_nr():
    """Uses the datetime module to grab the current date, get the iso calendar in (ISO year, ISO week number,
    ISO weekday) format and returns the week number."""
    return datetime.datetime.now().isocalendar()[1]
