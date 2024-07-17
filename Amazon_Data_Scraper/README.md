# Amazon Gaming Laptops Scraper

This project is a web scraper designed to extract details of gaming laptops from Amazon India. The scraper fetches the titles, prices, ratings, review counts, and availability of the products and saves this data to a CSV file.

## Features

- Extracts the title, price, rating, review count, and availability of gaming laptops.
- Saves the scraped data into a CSV file.
- Provides status updates during the scraping process.


## Usage
1.  Run the scraper:
      python scraper.py
2.  The script will print status updates as it processes each product link.
3.  The extracted data will be saved to amazon_data.csv.
    
## Code Overview
- get_title(soup): Extracts the product title.
- get_price(soup): Extracts the product price.
- get_rating(soup): Extracts the product rating.
- get_review_count(soup): Extracts the number of reviews.
- get_availability(soup): Extracts the product availability.

## Example Output
The scraper will create a CSV file with the following columns:

Title
Price
Rating
Reviews
Availability
