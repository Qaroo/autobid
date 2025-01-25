import requests
#response {'status': 0, 'message': 'eyJ0eXAiOiJqd3QiLCJhbGciOiJIUzI1NiJ9.eyJmaXJzdF9rZXkiOiI3MjM0NSIsInNlY29uZF9rZXkiOiIzODMzMzMxIiwiaXNzdWVkQXQiOiIyMy0wMS0yMDI1IDE0OjI5OjIwIiwidHRsIjo2MzA3MjAwMH0.BDKP-U2A7aVwMLx9On1e1c7h8EQskPIr4HDRXdvnkn8', 'expiration_date': '23/01/2027 14:29:20'}
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
    else:
        print(f"Failed with status code {response.status_code}")
        print(response.text)  # For additional error details

send_sms(["0533349945"],"2")


#Sending sms on:
#Mechanic side:
#new relvent repair
#Offer accepted

#Customer side:
#You got new offer
#When the car is ready.
#When the mechanic started working on the car

