from flask import Flask, render_template, request, redirect, send_file
import os
import json
import pandas as pd
from generate_random_sensor_data import generate_and_save_data
from analyze_uploaded_data import analyze_and_save_data

app = Flask(__name__)

# [1] 홈 화면: index.html
@app.route("/")
def home():
    return render_template("index.html")

# [2] 랜덤 센서 데이터 생성 및 다운로드
@app.route("/generate")
def generate_csv():
    file_path = generate_and_save_data()
    return send_file(file_path, as_attachment=True)

# [3] 업로드한 csv 파일 분석 후 status 추가 → 분석된 파일 다운로드
@app.route("/analyze", methods=["GET", "POST"])
def analyze():
    if request.method == "POST":
        file = request.files["file"]
        file_path = os.path.join("data", file.filename)
        file.save(file_path)

        analyzed_file_path = analyze_and_save_data(file_path)
        return send_file(analyzed_file_path, as_attachment=True)
    return render_template("analyze.html")

# [4] 분석된 csv 파일을 시각화
@app.route("/visualize", methods=["GET", "POST"])
def visualize():
    if request.method == "POST":
        file = request.files["file"]
        file_path = os.path.join("data", file.filename)
        file.save(file_path)

        df = pd.read_csv(file_path)
        chart_data = {
            "labels": df["timestamp"].tolist(),
            "vibration": df["vibration"].tolist(),
            "temperature": df["temperature"].tolist(),
            "rotation_speed": df["rotation_speed"].tolist(),
            "status": df["status"].tolist()
        }
        return render_template("visualize.html", data=json.dumps(chart_data))

    return render_template("visualize.html")

if __name__ == "__main__":
    app.run(debug=True)
