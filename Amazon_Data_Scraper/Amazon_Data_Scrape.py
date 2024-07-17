import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def get_title(soup):
    try:
        title = soup.find("span", attrs={"id":'productTitle'})
        title_value = title.text
        title_string = title_value.strip()
    except AttributeError:
        title_string = ""
    return title_string

def get_price(soup):
    try:
        price = soup.find("span", attrs={'class':'a-price-whole'}).text.strip().rstrip('.')
    except AttributeError:
        price = ""
    return price

def get_rating(soup):
    try:
        rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
    except AttributeError:
        try:
            rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
        except:
            rating = ""	
    return rating

def get_review_count(soup):
    try:
        review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()
    except AttributeError:
        review_count = ""	
    return review_count

def get_availability(soup):
    try:
        available = soup.find("span", attrs={'class':'a-size-medium a-color-success'}).string.strip()
    except AttributeError:
        available = "Not Available"	
    return available

if __name__ == '__main__':

    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    }

    base_url = "https://www.amazon.in"

    URL = "https://www.amazon.in/s?k=gaming+laptop&crid=R6YSRQZN57FV&sprefix=gaming+lap%2Caps%2C255&ref=nb_sb_ss_pltr-sample-20_2_10"

    # HTTP Request
    print("Fetching main search page.......")
    webpage = requests.get(URL, headers=HEADERS)

    # Check if the request was successful
    if webpage.status_code != 200:
        print(f"Failed to fetch webpage. Status code: {webpage.status_code}")
        exit()

    # Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "html.parser")

    # Fetch links as List of Tag Objects
    links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})

    # Store the links
    links_list = []

    # Loop for extracting links from Tag Objects
    print("Extracting product links........")
    for link in links:
        links_list.append(link.get('href'))

    d = {"title":[], "price":[], "rating":[], "reviews":[],"availability":[]}
    
    # Loop for extracting product details from each link 
    for index, link in enumerate(links_list):
        try:
            full_url = base_url + link
            print(f"Processing URL {index+1}/{len(links_list)}")
            new_webpage = requests.get(full_url, headers=HEADERS)

            # Check if the request to the product page was successful
            if new_webpage.status_code != 200:
                print(f"Failed to fetch product page. Status code: {new_webpage.status_code}")
                continue
            
            new_soup = BeautifulSoup(new_webpage.content, "html.parser")

            # Function calls to display all necessary product information
            title = get_title(new_soup)
            price = get_price(new_soup)
            rating = get_rating(new_soup)
            review_count = get_review_count(new_soup)
            availability = get_availability(new_soup)

            # Append data to dictionary
            d['title'].append(title)
            d['price'].append(price)
            d['rating'].append(rating)
            d['reviews'].append(review_count)
            d['availability'].append(availability)
        
        except Exception as e:
            print(f"Error processing URL {full_url}: {str(e)}")
            continue  # Skip to the next URL in case of error
    
    # Convert dictionary to DataFrame
    amazon_df = pd.DataFrame.from_dict(d)

    # Drop rows where title is NaN
    amazon_df['title'] = amazon_df['title'].replace('', np.nan)
    amazon_df = amazon_df.dropna(subset=['title'])

    # Save DataFrame to CSV
    amazon_df.to_csv("amazon_data.csv", header=True, index=False)

    print("Process completed successfully. Data saved to amazon_data.csv.")

