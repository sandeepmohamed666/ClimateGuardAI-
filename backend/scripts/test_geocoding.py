from backend.services.weather_service import (
    get_coordinates
)

result = get_coordinates(
    "Kochi"
)

print(result)


print(get_coordinates("Kochi"))
print(get_coordinates("Mumbai"))
print(get_coordinates("Delhi"))
print(get_coordinates("Chennai"))
