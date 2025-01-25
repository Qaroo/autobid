from flask import Flask, jsonify, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def find_car(car_id):
    url = f"https://autoboom.co.il/api/check_car/{car_id}?translation=he&size[]=300x300&size[]=200x200&size[]=800x800&size[]=1200x1200"

    res = requests.get(url)
    #print(res.request.headers)
    json = res.json()
    #print(json)
    json = json["success"]
    name = json["mark"]["mark_name"]
    model = json["model"]["model_name"]
    year = json["car"]["production_year"]["value"]
    engine = json["modification"]["engine_number"]["value"]
    transmission = json["modification"]["transmission"]["value"][0]["dval_name"]
    xa = {
        "name":name,
        "model": model,
        "year": year,
        "engine": engine,
        "transmission": name,
    }
    return ({"message": "Success!", "data":xa})

token = "eyJ0eXAiOiJqd3QiLCJhbGciOiJIUzI1NiJ9.eyJmaXJzdF9rZXkiOiI3MjM0NSIsInNlY29uZF9rZXkiOiIzODMzMzMxIiwiaXNzdWVkQXQiOiIyMy0wMS0yMDI1IDE0OjI5OjIwIiwidHRsIjo2MzA3MjAwMH0.BDKP-U2A7aVwMLx9On1e1c7h8EQskPIr4HDRXdvnkn8"
url = "https://019sms.co.il/api/test"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + token
}
def send_sms(phones, message_code):
    messages = {
        '0': "התקבלה בקשת תיקון חדשה, לחץ על הקישור על מנת לצפות בפרטים.",
        '1': "הצעת מחיר שהגשת התקבלה, לחץ על הקישור כדי לצפות בפרטים.",
        "2": "התקבלה הצעת מחיר חדשה לבקשה שהעלת, לחץ על הקישור על מנת לצפות בפרטים.",
        "3": "הרכב שלך מוכן, תאם עם המוסך על מנת לאסוף אותו",
        "4": "המוסך התחיל לעבוד על הרכב שלך, שים לב לעקוב אחרי הסטטוס שלו באתר."
    }
    message = messages[message_code]
    phoneData = []
    for phone in phones:
        phoneData.append({"_": phone,})

    data = {
      "sms": {
        "user": {
          "username": "AutobidService",
        },
        "source": "0505506566",
        "destinations": {
        "phone": phoneData,
        },
        "message": message,
      }
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        print("Request was successful!")
        print(response.json())  # For JSON response
        return jsonify({"message": "ההודעה נשלחה בהצלחה"}), 200
    else:
        print(f"Failed with status code {response.status_code}")
        print(response.text)  # For additional error details
        return jsonify({"message": "הייתה שגיאה בשליחת ההודעה"}), 500


@app.route('/')
def home():
    return jsonify({"message": "Welcome to my Flask App!!!!"})

@app.route('/findcar/<id>')
def findcar(id):
    return jsonify(find_car(id))

@app.route('/messagesystem', methods=["POST"])
def sending_sms(id):
    phones = request.json.get("receivers")
    message_type = request.json.get("type")
    if not phones or not message_type:
        return jsonify({"message": "הייתה שגיאה בשליחת ההודעה, שדה שגוי"}), 500
    status = send_sms(phones, message_type)
    return status

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    #app.run()
