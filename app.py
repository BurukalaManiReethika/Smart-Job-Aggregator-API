from flask import Flask, request, jsonify
from scraper import get_jobs

app = Flask(__name__)

jobs_data = get_jobs()

@app.route("/")
def home():
    return "Job Aggregator API Running 🚀"

@app.route("/jobs", methods=["GET"])
def get_jobs_api():
    return jsonify(jobs_data)

if __name__ == "__main__":
    app.run(debug=True)
