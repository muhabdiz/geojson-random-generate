import json
import random
from datetime import datetime

start_time = datetime.now()


jumlah_titik = 200000 #sesauikan jumlah titik yang diinginkan
output_file = "random_points.geojson"

# Membuat FeatureCollection
feature_collection = {
    "type": "FeatureCollection",
    "features": []
}

# Generate titik acak
for i in range(jumlah_titik):
    longitude = random.uniform(-180, 180)
    latitude = random.uniform(-90, 90)
    
    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [longitude, latitude]
        },
        "properties": {
            "id": i+1,
            "description": f"Random Point {i+1}"
        }
    }
    
    feature_collection["features"].append(feature)

    # Progress report setiap 50,000 titik
    if (i+1) % 50000 == 0:
        print(f"Generated {i+1} points...")

# Menulis ke file GeoJSON
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(feature_collection, f, separators=(',', ':'))

end_time = datetime.now()
print("\nCompleted!")
print(f"Total points generated: {jumlah_titik}")
print(f"File saved as: {output_file}")
print(f"Start time: {start_time}")
print(f"End time: {end_time}")
print(f"Execution time: {end_time - start_time}")