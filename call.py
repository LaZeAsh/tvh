# Download the helper library from https://www.twilio.com/docs/python/install
import os
from dotenv import load_dotenv
load_dotenv()
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
class Phone:
    def dial(self, person_name, activity_type, activity_location, activity_time, activity):
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        print(account_sid)
        print(auth_token)
        client = Client(account_sid, auth_token)

        call = client.calls.create(
            twiml=f'<Response><Say>This is an automated message, {person_name} would like to book an {activity_type} at {activity_location} on {activity_time} for {activity}. Press 1 to approve, Press 2 to suggest an alternate availability</Say><Gather numDigits="1" action="https://6f83-50-211-203-150.ngrok-free.app/gather-handler" method="POST"></Gather></Response>',
            to='+19257388240',
            from_='+18336202568'
        )