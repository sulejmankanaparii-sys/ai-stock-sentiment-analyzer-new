from flask import Blueprint, request, jsonify, render_template
from webapp.services.pipeline import run_pipeline

analyze_bp = Blueprint("analyze", __name__)

@analyze_bp.route("/")
def home():
    return render_template("index.html")


@analyze_bp.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    ticker = data.get("ticker")
    source = data.get("source")
    start_date = data.get("start_date")
    end_date = data.get("end_date")

    result = run_pipeline(ticker, source, start_date, end_date)

    return jsonify(result)