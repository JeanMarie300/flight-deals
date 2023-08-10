import requests
import os


class FlightSearch:
    def __init__ (self):
        self.endpoint= os.getenv('KIWI_ENDPOINT')
        self.api_key = os.getenv('KIWI_API_KEY')

    def getCityCode(self,cityName):
        url = self.endpoint + "locations/query"

        header = {
            'apikey':  self.api_key,
            'accept': 'application/json'
        }

        parameters = {
            'term':cityName,
            'location_types':'city',
            'limit':1
        }

        response = requests.get(url=url, headers=header, params=parameters)
        cityCode = response.json()['locations'][0]['code']
        return cityCode

    def getCheapestFlight(self, flight_parameters):

        url = self.endpoint + "search"

        header = {
            'apikey':  self.api_key,
            'accept': 'application/json'
        }

        parameters = {
            'fly_from':flight_parameters['fly_from'],
            'date_from':flight_parameters['from_date'],
            'date_to':flight_parameters['to_date'],
            'fly_to': flight_parameters['fly_to'],
            'curr':'CAD',
            'price_from':0,
            'price_to':flight_parameters['min_price'],
            'return_from':flight_parameters['from_date'],
            'return_to':flight_parameters['to_date'],
            'limit':1
        }

        response = requests.get(url=url, headers=header, params=parameters)

        return response.json()['data']




