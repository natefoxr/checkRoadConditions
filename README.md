# This program checks if the road conditions for highway 80 in Northern California & Sierra Nevada is open

## If the road conditions are set to not closed it will send a text message through Twillo SMS notification service

### Install the following packages in order to run this program:

- `pip3 install twilio`
- `pip3 install dotenv-python`

### To set this up on your own machine clone the repo and create a .env file with the following infomation:

- `SID="<Twilio SID>"`
- `AUTH="<Twilio Auth token>"`
- `PERSONAL_NUMBER="<The phone number that will recieve notifications>"`
- `TWILIO_NUMBER="<The Twilio number associateds with your account>"`

#### Run the command `python3 roadconditions.py`


