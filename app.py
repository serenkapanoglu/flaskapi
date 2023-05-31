from flask import Flask, render_template, request

import requests

API_BASE_URL="https://www.mapquestapi.com/geocoding/v1"

key = '4WiuDGgyNC6lAp04txicEbLMUf53z500'

app = Flask(__name__)

@app.route('/')
def show_addres_form():
    return render_template("address_form.html")

@app.route('/geocode')
def get_location():
    address = request.params["address"]
    res = requests.get(f"{API_BASE_URL}/address", params={'key':key, 'location':address})
    
    data = res.json()
    lat = data["results"][0]['locations'][0]['latLng']['lat']
    lng = data["results"][0]['locations'][0]['latLng']['lat']
    
    print('******************************************')
    
    print(lat, lng)