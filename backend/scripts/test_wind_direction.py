from backend.preprocessing.inference_pipeline import *

result = create_wind_direction_features(
    280
)

print(result)

print(
    sum(
        result.values()
    )
)
def create_default_region_features():

    return {
        f"region_{i}": 0
        for i in range(1, 33)
    }


def create_default_timezone_features():

    return {
        "timezone_1": 0,
        "timezone_2": 0
    }


def create_default_moon_features():

    moon = {
        "moon_illumination": 50
    }

    for i in range(1, 8):
        moon[f"moon_phase_{i}"] = 0

    moon["moon_phase_1"] = 1

    return moon


def create_default_day_length():

    return {
        "day_length_minutes": 720
    }

