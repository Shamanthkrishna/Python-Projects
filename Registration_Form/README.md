# Registration Form

## Overview

This application is a user-friendly registration form built using Python with Tkinter for the GUI and `tkcalendar` for date selection. It allows users to input personal, professional, and educational information, and saves the data to a CSV file upon submission.
**Note:** The Tkinter part of the registration form was generated based on required conditions using AI.

## Features

- **Basic Information**: First Name, Last Name, Email, Mobile Number
- **Address**: Multi-line text input
- **Personal Information**: Gender (Male/Female), Date of Birth (select from calendar or enter manually), Nationality, Blood Group
- **Professional Information**: Job Title, Company, Industry
- **Educational Information**: Highest Level of Education, Institution Attended, Field of Study
- **Additional Information**: Interests, Skills, Emergency Contact
- **Scrollable Form**: The form is scrollable to handle lengthy input fields.
- **CSV Export**: Data entered is saved to `registration_data.csv`.
- **Field Clearing**: All fields are cleared after registration.

## Requirements

- Python 3.x
- `tkinter`
- `tkcalendar`
- `csv`

## Installation

1. Clone or download this repository.
2. Install the required packages if not already installed:

    ```bash
    pip install tkcalendar
    ```

3. Run the application:

    ```bash
    python registration_form.py
    ```

## Usage

1. Open the application.
2. Fill out the registration form with your details.
3. Click the "Register" button to submit the form.
4. After submission, the form will clear all fields, and the data will be saved to `registration_data.csv`.

## Notes

- Ensure that all fields are filled out before submitting.
- The date of birth can be entered manually or selected from the calendar.

