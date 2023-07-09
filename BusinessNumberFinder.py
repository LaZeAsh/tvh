import cohere
import pandas as pd
from cohere.responses.classify import Example
co = cohere.Client('tfP85u2rk56RQf57kgAdGnk0rcmJHwgr0owaUGlG')

examples = [
    Example("Do you have any vegetarian options?", "Restaurant reservation"),
    Example("Can I make a reservation for two at 7 PM?", "Restaurant reservation"),
    Example("What is the dress code for your restaurant?", "Restaurant reservation"),
    Example("Is there outdoor seating available?", "Restaurant reservation"),
    Example("Do you offer any special dietary accommodations?", "Restaurant reservation"),
    Example("Can you recommend a good restaurant nearby?", "Restaurant reservation"),
    Example("Are children allowed in the restaurant?", "Restaurant reservation"),
    Example("Can I request a private dining area for a group?", "Restaurant reservation"),
    Example("What are your cancellation policies for reservations?", "Restaurant reservation"),
    Example("Do you have any gluten-free options?", "Restaurant reservation"),

    Example("Do you have any available appointments this week?", "Barber shop reservation"),
    Example("Can I book a haircut and beard trim together?", "Barber shop reservation"),
    Example("How long does a typical appointment last?", "Barber shop reservation"),
    Example("What are your opening hours?", "Barber shop reservation"),
    Example("Do you accept walk-ins or is an appointment necessary?", "Barber shop reservation"),
    Example("Can I request a specific barber for my appointment?", "Barber shop reservation"),
    Example("What are your prices for different hair services?", "Barber shop reservation"),
    Example("Is there parking available near the barber shop?", "Barber shop reservation"),
    Example("Do you offer any discounts for repeat customers?", "Barber shop reservation"),
    Example("Can I bring my cat for shaving during the appointment?", "Barber shop reservation"),

    Example("When is the earliest health appointment available?", "Medical clinic appointment"),
    Example("How long does a medical appointment usually take?", "Medical clinic appointment"),
    Example("Can I schedule a health appointment online?", "Medical clinic appointment"),
    Example("What documents or information should I bring for the appointment?", "Medical clinic appointment"),
    Example("How can I check the status of my appointment?", "Medical clinic appointment"),
    Example("Do you offer telemedicine appointments?", "Medical clinic appointment"),
    Example("Are there any specific preparations I need to make before the medical appointment?", "Medical clinic appointment"),
    Example("What should I do if I need to reschedule my medical appointment?", "Medical clinic appointment"),
    Example("Can I request a same-day medical appointment?", "Medical clinic appointment"),
    Example("Are there any restrictions for health appointment cancellations?", "Medical clinic appointment"),

    Example("Do you have any available appointments this week?", "Dental clinic appointment"),
    Example("Can I schedule a teeth cleaning appointment?", "Dental clinic appointment"),
    Example("What are your office hours?", "Dental clinic appointment"),
    Example("Do you offer emergency dental services?", "Dental clinic appointment"),
    Example("What insurances do you accept?", "Dental clinic appointment"),
    Example("Are there any specific instructions before a dental appointment?", "Dental clinic appointment"),
    Example("Can I bring my X-rays from a previous dentist?", "Dental clinic appointment"),
    Example("Do you provide pediatric dental services?", "Dental clinic appointment"),
    Example("How much does a dental check-up cost?", "Dental clinic appointment"),
    Example("Can I request a specific dentist for my appointment?", "Dental clinic appointment"),

    Example("Do you have any available appointments this week?", "Spa reservation"),
    Example("What services do you offer at your spa?", "Spa reservation"),
    Example("What are your spa's operating hours?", "Spa reservation"),
    Example("Do you offer couples' massages?", "Spa reservation"),
    Example("Can I request a specific therapist for my treatment?", "Spa reservation"),
    Example("Do you have any special promotions or discounts?", "Spa reservation"),
    Example("Can I bring my own products for the treatment?", "Spa reservation"),
    Example("What is the cancellation policy for spa reservations?", "Spa reservation"),
    Example("Are children allowed in the spa?", "Spa reservation"),
    Example("Do you offer gift certificates for spa treatments?", "Spa reservation"),

    Example("What are your available time slots for personal training?", "Personal trainer appointment"),
    Example("Can I book a group session with my friends?", "Personal trainer appointment"),
    Example("How long is a personal training session?", "Personal trainer appointment"),
    Example("What types of exercises and workouts do you offer?", "Personal trainer appointment"),
    Example("Do you provide nutritional guidance as part of the training?", "Personal trainer appointment"),
    Example("Can I choose the location for the training session?", "Personal trainer appointment"),
    Example("What is the cost of personal training sessions?", "Personal trainer appointment"),
    Example("Can I schedule a trial session before committing?", "Personal trainer appointment"),
    Example("Do you offer virtual personal training sessions?", "Personal trainer appointment"),
    Example("What is your policy for rescheduling or canceling personal training appointments?", "Personal trainer appointment"),

    Example("Can I schedule an appointment for a tattoo?", "Tattoo studio appointment"),
    Example("What is the minimum age requirement for getting a tattoo?", "Tattoo studio appointment"),
    Example("Do you have any tattoo artists specialized in a particular style?", "Tattoo studio appointment"),
    Example("What are the health and safety measures followed in your tattoo studio?", "Tattoo studio appointment"),
    Example("How long does it usually take to get a tattoo?", "Tattoo studio appointment"),
    Example("Do I need to provide any reference or design for the tattoo?", "Tattoo studio appointment"),
    Example("Can I bring a friend with me to the tattoo appointment?", "Tattoo studio appointment"),
    Example("What is your policy for tattoo touch-ups or corrections?", "Tattoo studio appointment"),
    Example("Do you offer tattoo removal services?", "Tattoo studio appointment"),
    Example("What are the aftercare instructions for a new tattoo?", "Tattoo studio appointment"),

    Example("Do you have any available car rentals for next week?", "Car rental reservation"),
    Example("What are the rental rates for your cars?", "Car rental reservation"),
    Example("What is the minimum age requirement for renting a car?", "Car rental reservation"),
    Example("What documents do I need to provide for car rental?", "Car rental reservation"),
    Example("Do you offer insurance coverage for the rental cars?", "Car rental reservation"),
    Example("What is your policy for late returns or extensions?", "Car rental reservation"),
    Example("Is there a mileage limit for the rental cars?", "Car rental reservation"),
    Example("Can I rent a car for a one-way trip?", "Car rental reservation"),
    Example("Do you have any luxury or specialty cars available?", "Car rental reservation"),
    Example("Are there any additional fees or charges for the car rental?", "Car rental reservation"),

    Example("Do you have any available truck rentals for this weekend?", "Truck rental reservation"),
    Example("What are the dimensions of your rental trucks?", "Truck rental reservation"),
    Example("Do you provide loading equipment with the truck rental?", "Truck rental reservation"),
    Example("What is the maximum weight capacity of your trucks?", "Truck rental reservation"),
    Example("Do you offer insurance coverage for the rental trucks?", "Truck rental reservation"),
    Example("What is your policy for late returns or extensions?", "Truck rental reservation"),
    Example("Is there a mileage limit for the rental trucks?", "Truck rental reservation"),
    Example("Can I rent a truck for a one-way trip?", "Truck rental reservation"),
    Example("Do you have any additional fees or charges for the truck rental?", "Truck rental reservation"),
    Example("What are your rates for truck rentals?", "Truck rental reservation"),
    
    Example("Do you have any available storage room rentals?", "Storage room rental reservation"),
    Example("What are the sizes and prices of your storage rooms?", "Storage room rental reservation"),
    Example("Do you offer climate-controlled storage rooms?", "Storage room rental reservation"),
    Example("Is there 24-hour access to the storage rooms?", "Storage room rental reservation"),
    Example("What is your policy for monthly rental payments?", "Storage room rental reservation"),
    Example("Do you provide packing supplies for storage?", "Storage room rental reservation"),
    Example("Can I switch to a larger or smaller storage room if needed?", "Storage room rental reservation"),
    Example("Is there a minimum rental duration for the storage rooms?", "Storage room rental reservation"),
    Example("What security measures are in place for the storage facility?", "Storage room rental reservation"),
    Example("Do you offer insurance coverage for the stored items?", "Storage room rental reservation"),
    
    Example("What are your operating hours?", "Museum visit"),
    Example("What is the admission fee for adults and children?", "Museum visit"),
    Example("Do you offer guided tours of the museum?", "Museum visit"),
    Example("Are there any temporary exhibitions currently?", "Museum visit"),
    Example("Is photography allowed inside the museum?", "Museum visit"),
    Example("Do you have a museum cafe or restaurant?", "Museum visit"),
    Example("Is there parking available near the museum?", "Museum visit"),
    Example("Are there any discounts for students or seniors?", "Museum visit"),
    Example("Can I bring my own food or drinks into the museum?", "Museum visit"),
    Example("Do you have a gift shop with museum souvenirs?", "Museum visit"),
    
    Example("What are your opening hours?", "Art gallery visit"),
    Example("Is there an admission fee for visiting the art gallery?", "Art gallery visit"),
    Example("Do you have any ongoing art exhibitions?", "Art gallery visit"),
    Example("Are there any upcoming artist talks or workshops?", "Art gallery visit"),
    Example("Can I purchase the exhibited artwork?", "Art gallery visit"),
    Example("Do you offer art classes or courses?", "Art gallery visit"),
    Example("Is photography allowed inside the art gallery?", "Art gallery visit"),
    Example("Are there any guided tours of the art gallery?", "Art gallery visit"),
    Example("Do you have a gift shop with art-related items?", "Art gallery visit"),
    Example("Can I rent the art gallery for private events?", "Art gallery visit"),
    
    Example("Do you have any available boat tickets for tomorrow?", "Boat ticket reservation"),
    Example("What is the departure time for the boat?", "Boat ticket reservation"),
    Example("What is the duration of the boat trip?", "Boat ticket reservation"),
    Example("Are there any specific instructions for boarding the boat?", "Boat ticket reservation"),
    Example("Do you offer any guided tours during the boat trip?", "Boat ticket reservation"),
    Example("Can I bring my own food and drinks on the boat?", "Boat ticket reservation"),
    Example("Is there a designated seating arrangement on the boat?", "Boat ticket reservation"),
    Example("What is your policy for cancellation or rescheduling of boat tickets?", "Boat ticket reservation"),
    Example("Do you offer any discounts for group bookings?", "Boat ticket reservation"),
    Example("Is there parking available near the boat departure point?", "Boat ticket reservation"),
     Example("Do you have any available rooms for the specified dates?", "Hotel reservation"),
    Example("What are the rates for a standard room?", "Hotel reservation"),
    Example("Do you offer complimentary breakfast for hotel guests?", "Hotel reservation"),
    Example("Can I request a non-smoking room?", "Hotel reservation"),
    Example("Is there a fitness center in the hotel?", "Hotel reservation"),
    Example("What is your cancellation policy for hotel reservations?", "Hotel reservation"),
    Example("Do you provide airport transportation for hotel guests?", "Hotel reservation"),
    Example("Are pets allowed in the hotel?", "Hotel reservation"),
    Example("Can I request a late check-out?", "Hotel reservation"),
    Example("What amenities are included in the room?", "Hotel reservation"),

    Example("Do you have any available flights for the specified dates?", "Plane trip reservation"),
    Example("What is the cost of a round-trip ticket?", "Plane trip reservation"),
    Example("Are there any direct flights to my destination?", "Plane trip reservation"),
    Example("What is the baggage allowance for the flight?", "Plane trip reservation"),
    Example("Can I choose my seat on the plane?", "Plane trip reservation"),
    Example("What is the in-flight meal policy?", "Plane trip reservation"),
    Example("Do you offer any entertainment options on the plane?", "Plane trip reservation"),
    Example("Is there Wi-Fi available during the flight?", "Plane trip reservation"),
    Example("What is your policy for flight changes or cancellations?", "Plane trip reservation"),
    Example("Are there any discounts for children or seniors?", "Plane trip reservation")
]

inputs = [
    input("What is your request? ")
]

response = co.classify(
    model='large', 
    inputs=inputs,  
    examples=examples
)
predictions = response.classifications
if predictions:
    max_prediction = max(predictions, key=lambda x: x.confidence)
#     print(f"Prediction: {max_prediction.prediction}")
# else:
#     print("No predictions found.")
data = {
    'category_name': ['Restaurant reservation', 'Barber shop reservation', 'Medical clinic appointment', 'Dental clinic appointment',
                      'Spa reservation', 'Personal trainer appointment', 'Tattoo studio appointment', 'Car rental reservation',
                      'Truck rental reservation', 'Storage room rental reservation', 'Museum visit', 'Art gallery visit',
                      'Boat ticket reservation', 'Hotel reservation', 'Plane trip reservation'],
    'business_name': ["Nonni's Bistro", "Locals Barbershop", "Stanford Health Care", "Pleasanton Family Dentist",
                      "Element Spa", "Tri-Valley Trainer", "Lea Graf Tattoo", "Enterprise", "U-Haul", "Public Storage",
                      "Museum on Main", "Studio Seven Arts", "Harbor Bay Ferry", "Courtyard", "Rose Airport"],
    'phone_number': ['9256000411', '9252714225', '9258473000', '9254620760', '9258339338', '9257844511', '9255963876',
                     '9252015214', '5106326828', '9253998956', '9254622766', '9258464322', '5107695500', '9254631414', '9255980000']
}

df = pd.DataFrame(data)

# Example category name given
category_name = max_prediction.prediction
# Match the category name and retrieve the business name and phone number
matched_row = df[df['category_name'] == category_name]

if len(matched_row) > 0:
    business_name = matched_row['business_name'].iloc[0]
    phone_number = matched_row['phone_number'].iloc[0]
    print(f"The business name is {business_name} and ")
    print(f"the phone number is {phone_number}.")
else:
    print("No matching category found for the given category name.")