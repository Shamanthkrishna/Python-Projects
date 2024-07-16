# Finance Tracker

A Python application to manage personal finances, allowing users to record transactions, view summaries, and visualize income versus expenses over time.

## Features

- **Add Transactions**: Record income and expenses with date, amount, category (Credit or Debit), and description.
- **View Transactions**: Summarize transactions within specific date ranges.
- **Plot Visualization**: Visualize income and expenses trends over time.

## Credit

This project was inspired by the tutorial from Tech With Tim on YouTube: [Finance Tracker Tutorial](https://www.youtube.com/watch?v=Dn1EjhcQk64).

## Usage

1. **Setup**:
   - Clone the repository and navigate into the project directory.
   - Install dependencies: `pip install pandas matplotlib`.

2. **Run**:
   - Execute `python main.py`.
   - Follow prompts to add transactions, view summaries, and optionally plot data.

3. **Structure**:
   - **main.py**: Main application logic.
   - **data_entry.py**: Input validation utilities.
   - **finance_data.csv**: Persistent storage for transaction records.
