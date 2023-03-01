import requests
from datetime import datetime
from pytz import timezone
import pytz
import time
import os
from twilio.rest import Client
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

def sendMessage(road):
    client = Client(os.getenv("SID"), os.getenv("AUTH"))

    message = client.messages.create(
    from_ = os.getenv("TWILIO_NUMBER"),
    body = '{} is Open'.format(road),
    to = os.getenv("PERSONAL_NUMBER")
    )

    print(message.sid)

def parseAndDisplay(info):
    date_format='%m/%d/%Y %H:%M:%S %Z'
    date = datetime.now(tz=pytz.utc)
    date = date.astimezone(timezone('US/Pacific'))
    print(date.strftime(date_format))
    cleantext = BeautifulSoup(info, features="html.parser").text
    print(cleantext)
    return True

def checkRoad(road):
    data= {
        'roadnumber': road
        }
    r = requests.post('https://roads.dot.ca.gov/roadscell.php', data=data)

    info = r.text.split('<p>')

    for i in info:
        if road == '80':
            if "IN THE NORTHERN CALIFORNIA AREA & SIERRA NEVADA" in i:
                if "CLOSED" not in i:
                    sendMessage(road)
                    return False
                else:
                    return parseAndDisplay(i)
        elif road == '50':
            if "IN THE SACRAMENTO VALLEY & THE LAKE TAHOE BASIN" in i:
                if "CLOSED" not in i:
                    sendMessage(road)
                    return False
                else:
                    return parseAndDisplay(i)

continueLoop = True
road_number = input("Would you like to check 50 or 80 (enter 50 or 80)?: ")

while continueLoop:
    continueLoop = checkRoad(road_number)
    time.sleep(15)