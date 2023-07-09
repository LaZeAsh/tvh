from flask import Flask, request
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
final_time=""
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly', 'https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/calendar.events']
@app.route('/gather-handler', methods=['POST'])
def gather_handler():
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    # Retrieve the Digits parameter from the Twilio request
    digits = request.form['Digits']
    
    # Process the user's input (you can customize this based on your application's logic)
    if digits == '1':
        # response_text = f"You entered 1, {main.activity_type} for {main.person_name} at {main.activity_time} has been confirmed, if you believe there has been a mistake please call {main.phone_number}"
        response_text = f"<Response><Say>You entered 1, appointment for Ayush at 7:00 PM has been confirmed, if you believe there has been a mistake please call 9 2 5 7 3 8 8 2 4 0</Say></Response>"
        # send message to application code
        message = client.messages \
                .create(
                     body="Hello Ayush, your appointment at Pleasanton Barber Shop has been confirmed for 7:00 PM, look forward to seeing you there!",
                     from_='+18336202568',
                     to='+19257388240'
                 )
        main()
    elif digits == '2':
        response_text=f'<Response><Say>Press 1 for 6:00 PM, Press 2 for 8:00 PM, or Press 3 for none of the above</Say><Gather numDigits="1" action="https://a6fe-50-211-203-150.ngrok-free.app/time-handle" method="POST"></Gather></Response>'    # Generate the TwiML response to send back to Twilio
    twiml_response = f"""{response_text}"""
    return twiml_response, 200, {'Content-Type': 'application/xml'}

@app.route('/time-handle', methods=['POST'])
def time_handler():
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    # Retrieve the Digits parameter from the Twilio request
    digits = request.form['Digits'] 

    if digits == '1':
        response_text = f"You entered 1, Ayush has been informed about 6:00 PM appointment and you will be updated soon, if you believe there has been a mistake please call 9 2 5 7 3 8 8 2 4 0"
        message = client.messages \
        .create(
                body="Hello Ayush, your appointment at Pleasanton Barber Shop was NOT scheduled for 7:00 PM, although an alternate time of 6:00 PM is available, reply with Y if you would like to schedule for 6:00 PM",
                from_='+18336202568',
                to='+19257388240'
            )
    elif digits == '2':
        response_text = f"You entered 2, Ayush has been informed about 8:00 PM appointment and you will be updated soon, if you believe there has been a mistake please call 9 2 5 7 3 8 8 2 4 0"
        message = client.messages \
        .create(
                body="Hello Ayush, your appointment at Pleasanton Barber Shop was NOT scheduled for 7:00 PM, although an alternate time of 8:00 PM is available, reply with Y if you would like to schedule for 8:00 PM",
                from_='+18336202568',
                to='+19257388240'
            )
    elif digits == '3':
        response_text = f"You entered 3, Ayush has been informed that there are no appointments available an hour within the stated time, if you believe there has been a mistake please call 9 2 5 7 3 8 8 2 4 0"
        message = client.messages \
        .create(
                body="Hello Ayush, your appointment at Pleasanton Barber Shop was NOT scheduled for 7:00 PM, there were no times available in an hour increments of the time you wanted!",
                from_='+18336202568',
                to='+19257388240'
            )
    
    twiml_response = f"""
        <Response>
            <Say>{response_text}</Say>
        </Response>
    """
    return twiml_response, 200, {'Content-Type': 'application/xml'}

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
        # calendar = {
        #     'summary': 'calendarSummary',
        #     'timeZone': 'America/Los_Angeles',
        #     'description': 'This is an event',

        # }

        # created_calendar = service.calendars().insert(body=calendar).execute()

                # print (created_calendar['id'])
        event = {
        'summary': 'Haircut',
        'location': 'Pleasanton Barber Shop',
        'description': '',
        'start': {
            'dateTime': '2023-07-09T07:00:00-08:00',
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': '2023-07-09T07:00:00-08:00',
            'timeZone': 'America/Los_Angeles',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=2'
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
            ],
        },
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        print('Event created: %s' % (event.get('htmlLink')))
        # # Call the Calendar API
        # now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        # print('Getting the upcoming 10 events')
        # events_result = service.events().list(calendarId='primary', timeMin=now,
        #                                       maxResults=10, singleEvents=True,
        #                                       orderBy='startTime').execute()
        # events = events_result.get('items', [])

        # if not events:
        #     print('No upcoming events found.')
        #     return

        # # Prints the start and name of the next 10 events
        # for event in events:
        #     start = event['start'].get('dateTime', event['start'].get('date'))
        #     print(start, event['summary'])

    except HttpError as error:
        print('An error occurred: %s' % error)

if __name__ == '__main__':
    app.run()