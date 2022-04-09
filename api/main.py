from flask import Flask, jsonify, request
from modules.db import DBRequests

app = Flask(__name__)

@app.route("/add")
def add():
    short_url = request.args.get("short_url")
    full_url = request.args.get("full_url")
    
    res = DBRequests.add_url(
        short_url=short_url,
        full_url=full_url
    )

    if res:
        return jsonify(result="succses")
    return jsonify(result="url already exists")

@app.route("/<short_url>", methods=['GET'])
def home(short_url: str):
    res = DBRequests.get_url(short_url=short_url)
    return jsonify(res=res)

if __name__ == "__main__":
    app.run(debug=True)