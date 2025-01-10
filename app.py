from flask import Flask, jsonify
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

@app.route('/')
def home():
    return jsonify({"message": "Welcome to my Flask App!!!!"})

@app.route('/findcar/<id>')
def findcar(id):
    return jsonify(find_car(id))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    #app.run()
