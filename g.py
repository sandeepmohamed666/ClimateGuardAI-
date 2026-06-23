# # import os

# # for root, dirs, files in os.walk("."):
# #     for file in files:
# #         if file.endswith(".pkl"):
# #             print(os.path.join(root, file))

# import joblib

# mapping = joblib.load(
#     "models/rainfall_class_mapping.pkl"
# )

# print(type(mapping))
# print(mapping)

print(get_coordinates("Kochi"))
print(get_coordinates("Mumbai"))
print(get_coordinates("Delhi"))
print(get_coordinates("Chennai"))
