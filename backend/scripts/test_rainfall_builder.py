from backend.services.weather_service import *
from backend.preprocessing.inference_pipeline import *

location = get_coordinates("Kochi")

weather = get_weather_data(
    location["latitude"],
    location["longitude"]
)

air = get_air_quality_data(
    location["latitude"],
    location["longitude"]
)

features = build_rainfall_features(
    weather,
    air,
    location
)

print(
    "Feature Count:",
    len(features)
)


for key, value in features.items():
    print(key, value)
