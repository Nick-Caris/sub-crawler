from flask import Flask, jsonify
from sub_crawler.__main__ import crawl

app = Flask(__name__)

@app.route("/subs")
def subs():
    return jsonify(crawl())
