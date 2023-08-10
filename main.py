import os
from flight_search import FlightSearch
from data_manager import DataManager
from _datetime import *
from dateutil.relativedelta import relativedelta
from notification_manager import NotificationManager

start_period = datetime.now() + timedelta(days=1)

end_period = datetime.now() + relativedelta(months=+6)

start_period = start_period.strftime("%d/%m/%Y")
end_period = end_period.strftime("%d/%m/%Y")

data_manager = DataManager()

flight_search = FlightSearch()

notificationManager = NotificationManager()

sheet_data = data_manager.getSheetData()

for flight in sheet_data:

    flight_parameters = {
        'start_period':start_period,
        'to_date':end_period,
        'fly_from':os.getenv('FLY_FROM'),
        'fly_to':flight['iataCode'],
        'min_price':flight['lowestPrice']
    }
    cheapest_flight = flight_search.getCheapestFlight(flight_parameters)

    for flight_found in cheapest_flight:
        flight_details = {
            'price':flight_found["price"],
            'cityFrom':flight_found["cityFrom"],
            'flyFrom':flight_found["flyFrom"],
            'cityTo':flight_found["cityTo"],
            'flyTo':flight_found["flyTo"],
            'from_date':datetime.fromtimestamp(flight_found["route"][0]['dTime']).strftime("%Y-%m-%d"),
            'to_date':datetime.fromtimestamp(flight_found["route"][1]['dTime']).strftime("%Y-%m-%d")
        }
        notificationManager.sendNotification(flight_details)
