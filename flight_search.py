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
            'fly_to': flight_parameters['fly_to'],
            'date_from':flight_parameters['start_period'],
            'date_to':flight_parameters['to_date'],
            'curr':'CAD',
            "nights_in_dst_from":7,
            "nights_in_dst_to":28,
            'price_to':flight_parameters['min_price'],
            "one_for_city":1,
            'max_stopovers': flight_parameters['max_stopovers']
        }

        response = requests.get(url=url, headers=header, params=parameters)

        if len(response.json()['data']) == 0:
            parameters['max_stopovers'] = 2
            response = requests.get(url=url, headers=header, params=parameters)

        return response.json()['data']




