import requests


key = '4WiuDGgyNC6lAp04txicEbLMUf53z500'
response = requests.get('https://www.mapquestapi.com/geocoding/v1/address', 
             params={'key':key, 'location': 'Denver, CO'})