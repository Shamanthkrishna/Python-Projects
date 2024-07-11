import os
import random
import smtplib


def auto_email():
    user = input("Enter your Name >>: ")
    email = input("Enter your Email >>: ")
    message = (f"Dear {user}, Welcome to Automatic Email Sender Bot")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    # Browse to know How to Create App Password in Google, Then Enter the 16 digit password without spaces 
    s.login("Sender Mail ID","Sender App Password") 
    s.sendmail('Sender Mail ID', email, message)
    print("Email Sent!")


while True:
    auto_email()
    try_again = input("Do you want to Send Again? (y/n):").lower()
    if try_again != "y":
        break

print("Thanks for Using Auto Mail Sender Bot")
input("Press any key to exit....")

# OUTPUT

# Enter your Name >>: Shamanth Krishna
# Enter your Email >>: abcd@gmail.com
# Email Sent!

# <<<<< Mail recieved >>>>>
# Dear Shamanth Krishna, Welcome to Automatic Email Sender Bot
