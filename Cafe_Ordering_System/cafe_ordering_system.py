import csv
import uuid
import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Menu with items and their prices
menu = {
    "Tea": 20,
    "Coffee": 20,
    "Maggi": 40,
    "Pizza": 100,
    "Dosa": 45,
    "Iced Tea": 40,
    "Burger": 50,
    "Lime Soda": 30
}

# Greet the customer
print("Welcome to Cafe Mangalore")
print("We are delighted to have you here.")
print("Here's our menu. Enjoy a 10% discount on orders over Rs. 500!")
print("Menu")

# Display the menu items with their prices
menu_items = list(menu.keys())
for idx, item in enumerate(menu_items, 1):
    print(f"{idx}. {item}: Rs.{menu[item]}")

order_total = 0
order_summary = []  # To store the summary of the current order
order_history = []  # To store the history of all orders

# Ask for the customer's name
user_name = input("Please enter your name: ")

# Loop to take the customer's order
while True:
    # Ask for the item number
    item = int(input("Enter the number of the item you want to order: "))

    if 1 <= item <= len(menu_items):
        item_name = menu_items[item - 1]
        quantity = int(input(f"How many {item_name} would you like to order? "))
        order_cost = menu[item_name] * quantity
        order_total += order_cost
        order_summary.append((item_name, quantity, order_cost))
        order_history.append((item_name, quantity, order_cost))
        print(f"{quantity} {item_name}(s) Ordered Successfully")
    else:
        print("Invalid choice. Please try again.")

    # Ask if the customer wants to order anything else
    another_item = input("Do you want to order anything else? (y/n): ").lower()
    if another_item != "y":
        break

# Generate a unique order ID and receipt number
order_id = str(uuid.uuid4())
receipt_number = random.randint(1000, 9999)

# Display the order summary
print("\nOrder Summary:")
for item, quantity, cost in order_summary:
    print(f"{quantity} x {item}: Rs.{cost}")

# Calculate and display the total order amount
print(f"\nYour total order amount is: Rs.{order_total:.2f}")

# Apply a 10% discount if the total order amount exceeds Rs. 500
if order_total > 500:
    discount = order_total * 0.1  # 10% discount
    order_total -= discount
    print(f"\nDiscount applied: Rs.{discount:.2f}")

print(f"Final total after discount (if applicable): Rs.{order_total:.2f}")

# Ask for the payment method
payment_method = input("\nEnter your preferred payment method (Cash/Card): ").strip().capitalize()
print(f"Payment Method: {payment_method}")

# Save the order history to a CSV file
with open('order_history.csv', 'a', newline='') as csvfile:
    fieldnames = ['Order ID', 'User Name', 'Item', 'Quantity', 'Total Cost']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    if csvfile.tell() == 0:
        writer.writeheader()

    for item, quantity, cost in order_summary:
        writer.writerow({'Order ID': order_id, 'User Name': user_name, 'Item': item, 'Quantity': quantity, 'Total Cost': cost})

print("Your order history has been saved to 'order_history.csv'.")

# Ask if the customer wants to generate a receipt
generate_receipt = input("\nWould you like to generate a receipt? (y/n): ").lower()
if generate_receipt == "y":
    # Generate a PDF receipt
    receipt_filename = f"receipt_{order_id}.pdf"
    c = canvas.Canvas(receipt_filename, pagesize=letter)
    c.setFont("Helvetica", 12)
    c.drawString(100, 750, f"Cafe Mangalore Receipt")
    c.drawString(100, 735, f"Receipt Number: {receipt_number}")
    c.drawString(100, 720, f"Order ID: {order_id}")
    c.drawString(100, 705, f"Customer Name: {user_name}")
    c.drawString(100, 690, f"Payment Method: {payment_method}")
    
    c.drawString(100, 660, "Order Summary:")
    y_position = 640
    for item, quantity, cost in order_summary:
        c.drawString(100, y_position, f"{quantity} x {item}: Rs.{cost}")
        y_position -= 20
    
    c.drawString(100, y_position, f"Total Amount: Rs.{order_total:.2f}")
    
    if order_total > 500:
        c.drawString(100, y_position - 20, f"Discount Applied: Rs.{discount:.2f}")
        y_position -= 20

    c.drawString(100, y_position - 20, f"Final Amount: Rs.{order_total:.2f}")
    
    c.showPage()
    c.save()
    print(f"Your receipt has been saved as '{receipt_filename}'.")

# Thank the customer
print("\nThank you for your order! We hope you enjoy your meal.")
print("Have a wonderful day and come back soon!")
