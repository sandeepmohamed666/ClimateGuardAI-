import joblib

encoder = joblib.load(
    "models/heatwave_label_encoder.pkl"
)

print(type(encoder))

try:
    print(encoder.classes_)
except:
    print("No classes_ attribute")

