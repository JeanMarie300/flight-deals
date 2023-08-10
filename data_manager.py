import requests
import os

SHEET_ENDPOINT = os.getenv('SHEET_ENDPOINT')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
class DataManager:

    def __init__ (self):
        self.endpoint= os.getenv('SHEET_ENDPOINT')
        self.bearer_token = os.getenv('BEARER_TOKEN')

    def getSheetData(self):
        url = self.endpoint
        header = {
            'Authorization': 'Bearer ' + self.bearer_token
        }
        response = requests.get(url=url, headers=header)

        return response.json()['prices']

    def updateFileData(self, flight):

        url = self.endpoint + f'/{id}'
        print(url)
        header = {
            'Authorization': 'Bearer ' + self.bearer_token
        }
        body = {
            'price':{
                'iataCode': flight.iataCode
            }
        }

        response = requests.put(url=url, headers=header,json=body)

        return response.status_code
