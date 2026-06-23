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

df = align_rainfall_features(
    features
)

print(df.shape)

print(df.columns.tolist()[:25])
