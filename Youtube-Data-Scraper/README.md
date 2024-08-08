# YouTube Channel Data Extractor

## Overview

The **YouTube Channel Data Extractor** is a Python application that allows users to extract and analyze data from YouTube channels based on video URLs. This tool uses the PyTube library to fetch channel information and the Google YouTube API to retrieve channel statistics. Users can also export the collected data to a CSV file for further analysis.

## Features

- Extracts YouTube Channel IDs from video URLs.
- Fetches channel statistics including subscribers, views, and total videos.
- Provides an option to save the extracted data as a CSV file.
- User-friendly command-line interface.

## Requirements

- Python 3.x
- `google-api-python-client` library
- `pytube` library
- `pandas` library

You can install the required libraries using pip:

```bash
pip install google-api-python-client pytube pandas
```

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Create a Python Virtual Environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Obtain a YouTube API Key:**

   - Go to the [Google Developers Console](https://console.developers.google.com/).
   - Create a new project and enable the YouTube Data API v3.
   - Create an API key and replace the placeholder in `YT_Extracter.py`.

## Usage

1. **Run the Application:**

   ```bash
   python main.py
   ```

2. **Follow the Prompts:**

   - Enter the YouTube video URL when prompted.
   - Type 'exit' to finish inputting URLs.
   - Choose whether to save the collected data as a CSV file.

## File Structure

- `main.py`: The main script that runs the application and handles user input.
- `YT_Extracter.py`: Contains functions for extracting channel IDs and fetching channel statistics, as well as exporting data to CSV.

## Example

Here's a quick example of how to use the application:

1. Start the application:

   ```bash
   python main.py
   ```

2. Input a YouTube video URL:

   ```
   Please enter the YouTube video URL (or type 'exit' to quit): https://www.youtube.com/watch?v=BKSiFyCkDM0&t
   ```

3. Choose to save the data:

   ```
   Would you like to save this data as a CSV file? (y/n): y
   Enter filename for CSV export (default 'channel_data.csv'): my_channel_data.csv
   ```

4. The data will be saved to `my_channel_data.csv`.

## Contributing

Feel free to submit issues or pull requests to improve the project. For significant changes, please discuss them first by opening an issue.

## Contact

For any questions or suggestions, please reach out to [shamanthkrishna0@gmail.com](mailto:shamanthkrishna0@gmail.com).
