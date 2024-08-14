# Phone Number Details Parser

This Python project parses and extracts detailed information from phone numbers, including the formatted number, time zone, carrier, region, country, and number type. The results are saved to a CSV file, appending new entries without overwriting previous data.

## Features

- **Phone Number Parsing:** Extracts details such as formatted number, time zone, carrier, region, country, and number type.
- **CSV Logging:** Saves the extracted information to a CSV file (`phone_details.csv`), appending new data each time the script is run.
- **Batch Processing:** Allows processing of multiple phone numbers at once.
- **Error Handling:** Validates phone numbers and provides feedback if the number is invalid.
- **Customizable Output:** CSV file is structured with the header written only during the initial run.
- **Exception Handling:** Handles potential parsing errors and informs the user.

## Usage

1. **Run the Script:**

    To run the script, simply execute:

    ```bash
    python main.py
    ```

2. **Input:**
   
    Enter the phone number with the country code when prompted (e.g., `+91 63618 09012`).

3. **Output:**
   
    The script will parse the phone number and output details to the terminal. It will also append the data to `phone_details.csv`.

4. **CSV File Structure:**

    The CSV file will have the following columns:

    ```text
    Formatted Number,Time Zone,Carrier,Region,Country,Number Type
    ```

    Example:
    
    ```text
    Formatted Number,Time Zone,Carrier,Region,Country,Number Type
    +91 63618 09015,Asia/Calcutta,Reliance Jio,India,India,Mobile
    ```
