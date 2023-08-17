import os
from flight_search import FlightSearch
from data_manager import DataManager
from _datetime import *
from dateutil.relativedelta import relativedelta
from notification_manager import NotificationManager
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from customer_acquisition import CustomerAcquisition

data_manager = DataManager()

email_list = data_manager.getEmailListData( os.getenv('EMAIL_SHEET_ENDPOINT'), os.getenv('EMAIL_BEARER_TOKEN'))

flight_sheet_data = data_manager.getSheetData()

if len(email_list) == 0 :
    form_init = CustomerAcquisition()

start_period = datetime.now() + timedelta(days=1)
end_period = datetime.now() + relativedelta(months=+6)
start_period = start_period.strftime("%d/%m/%Y")
end_period = end_period.strftime("%d/%m/%Y")

flight_search = FlightSearch()

notificationManager = NotificationManager()

for flight in flight_sheet_data:

    flight_parameters = {
        'start_period':start_period,
        'to_date':end_period,
        'fly_from':os.getenv('FLY_FROM'),
        'fly_to':flight['iataCode'],
        'min_price':flight['lowestPrice'],
        'max_stopovers' : 0
    }
    cheapest_flight = flight_search.getCheapestFlight(flight_parameters)

    for flight_found in cheapest_flight:
        if len(flight_found["route"]) > 2:
            from_date = datetime.fromtimestamp(flight_found["route"][0]['dTime']).strftime("%Y-%m-%d")
            to_date = datetime.fromtimestamp(flight_found["route"][2]['dTime']).strftime("%Y-%m-%d")
        else:
            from_date = datetime.fromtimestamp(flight_found["route"][0]['dTime']).strftime("%Y-%m-%d")
            to_date = datetime.fromtimestamp(flight_found["route"][1]['dTime']).strftime("%Y-%m-%d")

        flight_details = {
            'price':flight_found["price"],
            'cityFrom':flight_found["cityFrom"],
            'flyFrom':flight_found["flyFrom"],
            'cityTo':flight_found["cityTo"],
            'flyTo':flight_found["flyTo"],
            'from_date':from_date,
            'to_date':to_date,
            'route':flight_found['route']
        }

        notificationManager.sendNotification(flight_details)
        #Notify the members of the email list
        for email in email_list:
            notificationManager.sendEmail(email['email'], flight_details)

