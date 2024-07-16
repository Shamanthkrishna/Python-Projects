from datetime import datetime


date_format = "%d-%m-%Y"
CATEGORIES = {"C": "Credit", "D":"Debit"}



def get_date(prompt, allow_default=False):
    date_str = input(prompt)

    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(date_str,date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid Date Format. Please enter the date in dd-mm-yyyy format")
        return get_date(prompt, allow_default)

def get_amount():
    try:
        amount = float(input("Enter the Amount: "))
        if amount <=0:
            raise ValueError("Amount must be a non-negative non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category = input("Enter the Category ('C' for Credit or 'D' for Debit): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print(":Invalid Category. Please enter 'C' for Credit and 'D' for Debit.")
    return get_category()


def get_description():
    return input("Enter a Description (Optional): ")
