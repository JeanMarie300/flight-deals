import requests
from twilio.rest import Client
import os
import smtplib
from _datetime import *

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        self.auth_token =  os.getenv('TWILIO_AUTH_TOKEN')
        self.to_phone_number = os.getenv('TO_PHONE_NUMBER')
        self.from_phone_number = os.getenv('FROM_PHONE_NUMBER')
        self.from_city_code = os.getenv('FROM_PHONE_NUMBER')
        self.message = ""

    def sendNotification(self, flight_details):
        self.updateMessage(flight_details)
        client = Client(self.account_sid, self.auth_token)
        client.messages.create(
            to=self.to_phone_number,
            from_=self.from_phone_number,
            body=self.message
        )

    def sendEmail(self, email_to, flight_details):
        self.updateMessage(flight_details)
        gmailAddress = "j41878235@gmail.com"
        gmailAppPassword = os.getenv("GMAIL_PASSWORD")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=gmailAddress, password=gmailAppPassword)
            connection.sendmail(
                from_addr=gmailAddress,
                to_addrs=email_to,
                msg=f"Subject:Flight Deals Alert \n\n {self.message}"
            )

    def updateMessage(self, flight_details):

        if len(flight_details['route']) > 2 :
            self.message = f'Sent from your Twilio trial account - \n Low price alert! Only {flight_details["price"]} to fly from \n' \
                           f'{flight_details["cityFrom"]} - {flight_details["flyFrom"]}  to {flight_details["cityTo"]} - {flight_details["flyTo"]}, from \n' \
                           f'{flight_details["from_date"]} - {flight_details["to_date"]} '\
                           f'The flight has one stop over in {flight_details["route"][0]["cityTo"]}'
            pass
        else:
            self.message = f'Sent from your Twilio trial account - \n Low price alert! Only {flight_details["price"]} to fly from \n' \
                           f'{flight_details["cityFrom"]} - {flight_details["flyFrom"]}  to {flight_details["cityTo"]} - {flight_details["flyTo"]}, from \n' \
                           f'{flight_details["from_date"]} - {flight_details["to_date"]} '









