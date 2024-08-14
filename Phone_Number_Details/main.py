import phonenumbers
from phonenumbers import timezone, geocoder, carrier
import csv
import os

# Function to parse and get details from phone number
def get_phone_details(number):
    phone = phonenumbers.parse(number)
    
    # Validation
    if not phonenumbers.is_valid_number(phone):
        print("The entered phone number is not valid.")
        return None
    
    # Extracting details
    formatted_number = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    time = timezone.time_zones_for_number(phone)
    car = carrier.name_for_number(phone, "en")
    reg = geocoder.description_for_number(phone, "en")
    country = geocoder.country_name_for_number(phone, "en")
    number_type_info = phonenumbers.number_type(phone)
    
    # Identify the number type
    if number_type_info == phonenumbers.PhoneNumberType.MOBILE:
        number_type = "Mobile"
    elif number_type_info == phonenumbers.PhoneNumberType.FIXED_LINE:
        number_type = "Fixed Line"
    else:
        number_type = "Other"
    
    print(f'Your {number_type}:{formatted_number}')
    print(f'Time-Zone: {time}')
    print(f'Carrier: {car}')
    print(f'Region: {reg}')
    print(f'Country: {country}')
    print(f'Number Type: {number_type}')

    return {
        "Formatted Number": formatted_number,
        "Time Zone": ', '.join(time),  # Joining list of time zones
        "Carrier": car,
        "Region": reg,
        "Country": country,
        "Number Type": number_type
    }

# Input from user
number = input("Enter your Number with Country Code: ")
details = get_phone_details(number)

if details:
    # Check if the CSV file exists
    file_exists = os.path.isfile('phone_details.csv')
    
    # Open the CSV file in append mode
    with open('phone_details.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=details.keys())
        
        # Write the header only if the file doesn't exist
        if not file_exists:
            writer.writeheader()
        
        # Write the data
        writer.writerow(details)
    
    print("Details appended to phone_details.csv")
