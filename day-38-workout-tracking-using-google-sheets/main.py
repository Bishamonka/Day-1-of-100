import os
import requests
import datetime

d = datetime.datetime.now()

NUTRITIONIX_APP_ID = os.environ["NUTRITIONIX_APP_ID"]
NUTRITIONIX_APP_KEY = os.environ["NUTRITIONIX_APP_KEY"]
NUTRITIONIX_API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_APP_KEY,
    "x-remote-user-id": "0",
}

parameters = {
    "query": input("What did you do today? (f.e. 'I ran 5 kilometers for 20 minutes')\n"),
    "gender": "male",
    "weight_kg": 82.5,
    "height_cm": 182.5,
    "age": 18,
}

nutritionix_response = requests.post(url=NUTRITIONIX_API_ENDPOINT, json=parameters, headers=nutritionix_headers)
print(nutritionix_response.text)
result = nutritionix_response.json()

today = d.strftime("%d/%m/%Y")
current_time = d.strftime("%X")

SHEETY_API_ENDPOINT = "https://api.sheety.co/f82b447acfd877e3493a06f45ebdefec/workouts/workouts"
SHEETY_BEARER_TOKEN = os.environ["SHEETY_BEARER_TOKEN"]

sheety_headers = {
    "Authorization": SHEETY_BEARER_TOKEN
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheety_response = requests.post(url=SHEETY_API_ENDPOINT, json=sheet_inputs, headers=sheety_headers)
    print(sheety_response.text)
