from flask import Flask, request
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
final_time=""
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
    elif digits == '2':
        response_text=f'<Response><Say>Press 1 for 6:00 PM, Press 2 for 8:00 PM, or Press 3 for none of the above</Say><Gather numDigits="1" action="https://6f83-50-211-203-150.ngrok-free.app/time-handle" method="POST"></Gather></Response>'    # Generate the TwiML response to send back to Twilio
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

if __name__ == '__main__':
    app.run()