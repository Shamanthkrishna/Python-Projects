# Cafe Mangalore Ordering System

## Overview:
This Python script enables customers to place orders at Cafe Mangalore. It provides an interactive menu selection, computes order totals, applies discounts, and offers the option to generate PDF receipts. The order history is saved in a CSV file for future reference.

## Features:
- Interactive menu display and item selection.
- Order customization with quantity input for each item.
- Calculation of total order amount and application of discounts (10% off orders over Rs. 500).
- Saving of order details (including unique order ID) in `order_history.csv`.
- Optional generation of detailed PDF receipts with order summary.

## Usage:
1. Run the script (`python cafe_ordering_system.py`).
2. Enter your name and select items from the displayed menu by entering the corresponding number.
3. Specify the quantity for each item.
4. Confirm if additional items are needed.
5. Choose a payment method (Cash or Card).
6. Opt to generate a receipt (PDF format).
7. Review the order summary and final amount.
8. Receive confirmation and a thank you message upon completion.

## Dependencies:
- Python 3.12.4
- `reportlab` library for PDF generation (`pip install reportlab`)

## Files:
- `cafe_ordering_system.py`: Main Python script for ordering and receipt generation.
- `order_history.csv`: CSV file containing saved order details.
- Receipts: Sample PDF files generated for each order (e.g., `receipt_<order_id>.pdf`).

## Notes:
- Ensure Python and the `reportlab` library are installed before running the script.
- Customize the menu and pricing in the `menu` dictionary within the script as needed.
- The script maintains simplicity while offering essential features for a small cafe ordering system.

## Author:
Shamanth Krishna

## Contact:
shamanthkrishna0@gmail.com
