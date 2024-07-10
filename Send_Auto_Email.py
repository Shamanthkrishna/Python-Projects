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


auto_email()

# OUTPUT

# Enter your Name >>: Shamanth Krishna
# Enter your Email >>: abcd@gmail.com
# Email Sent!

# <<<<< Mail recieved >>>>>
# Dear Shamanth Krishna, Welcome to Automatic Email Sender Bot