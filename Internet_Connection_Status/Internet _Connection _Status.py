import requests
from requests.exceptions import ConnectionError, Timeout
import time
import os

def internet_connection_test(urls=None, retries=3, timeout=10):
    if urls is None:
        urls = ['https://www.google.com/', 'https://www.amazon.in/', 'https://www.github.com/']
    
    for url in urls:
        for attempt in range(1, retries + 1):
            print(f'Attempt {attempt} to connect to {url} to determine internet connection status.')
            try:
                start_time = time.time()
                response = requests.get(url, timeout=timeout)
                response_time = time.time() - start_time
                
                if response.status_code == 200:
                    print(f'Connection to {url} was successful. Status code: {response.status_code}')
                    print(f'Response time: {response_time:.2f} seconds')
                    log_result(url, True, response_time)
                    break
                else:
                    print(f'Failed to connect to {url}. Status code: {response.status_code}')
                    log_result(url, False)
            except (ConnectionError, Timeout) as e:
                print(f'Attempt {attempt} failed: {str(e)}')
                log_result(url, False)
                if attempt == retries:
                    print(f'All {retries} attempts to connect to {url} failed.')
            except Exception as e:
                print(f'Attempt {attempt} failed with an unexpected error: {str(e)}')
                log_result(url, False)
                if attempt == retries:
                    print(f'All {retries} attempts to connect to {url} failed.')
                    
def log_result(url, success, response_time=None):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Define the path for the log file
    log_file_path = os.path.join(script_dir, 'connection_log.txt')
    
    with open(log_file_path, 'a') as log_file:
        if success:
            log_file.write(f'Success: Connected to {url} in {response_time:.2f} seconds\n')
        else:
            log_file.write(f'Failure: Could not connect to {url}\n')

internet_connection_test()
