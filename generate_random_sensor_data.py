import csv
import os
import random
from datetime import datetime, timedelta

def generate_and_save_data():
    num_entries = 100
    start_time = datetime(2025, 7, 25, 14, 0, 0)
    file_name = f"random_sensor_data_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
    file_path = os.path.join("data", file_name)

    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "vibration", "temperature", "rotation_speed"])
        for i in range(num_entries):
            timestamp = start_time + timedelta(seconds=i * 10)

            if i % 10 == 0:  # 이상값
                vibration = round(random.uniform(1.3, 2.0), 2)
                temperature = round(random.uniform(81, 95), 1)
                rotation_speed = random.randint(600, 850)
            else:  # 정상값
                vibration = round(random.uniform(0.3, 1.1), 2)
                temperature = round(random.uniform(60, 75), 1)
                rotation_speed = random.randint(1100, 1600)

            writer.writerow([
                timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                vibration,
                temperature,
                rotation_speed
            ])

    return file_path
