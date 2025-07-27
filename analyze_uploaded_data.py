import pandas as pd
import os

def analyze_and_save_data(file_path):
    df = pd.read_csv(file_path)

    def classify(row):
        # 간단한 이상 판별 기준
        if row["vibration"] > 1.2 or row["temperature"] > 80 or row["rotation_speed"] < 1000:
            return 1  # 이상
        return 0  # 정상

    df["status"] = df.apply(classify, axis=1)

    new_file_name = os.path.splitext(os.path.basename(file_path))[0] + "_analyzed.csv"
    new_file_path = os.path.join("data", new_file_name)
    df.to_csv(new_file_path, index=False)

    return new_file_path
