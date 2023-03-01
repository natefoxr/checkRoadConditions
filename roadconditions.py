import requests
import time
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

def sendMessage(road):
    client = Client(os.getenv("SID"), os.getenv("AUTH"))

    message = client.messages.create(
    from_ = os.getenv("TWILIO_NUMBER"),
    body = '{} is Open'.format(road),
    to = os.getenv("PERSONAL_NUMBER")
    )

    print(message.sid)

def checkRoad(road):
    data= {
        'roadnumber': road
        }
    r = requests.post('https://roads.dot.ca.gov/roadscell.php', data=data)

    info = r.text.split('<p>')

    for i in info:
        if "IN THE NORTHERN CALIFORNIA AREA & SIERRA NEVADA" in i:
            if "CLOSED" not in i:
                sendMessage(road)
                return False
            else:
                print(i)
                return True

continueLoop = True

while continueLoop:
    continueLoop = checkRoad('80')
    time.sleep(15)