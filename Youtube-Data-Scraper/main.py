# main.py
from YT_Extracter import *

def print_welcome_message():
    print("\nWelcome to the YouTube Channel Data Extractor!")
    print("This tool allows you to extract and analyze YouTube channel data from video URLs.")
    print("You can also save the data to a CSV file for further use.")
    print("You can enter as many YouTube video URLs as you want.")
    print("Type 'exit' when you are finished entering URLs.")
    print()

def get_user_input():
    while True:
        video_url = input("Please enter the YouTube video URL (or type 'exit' to quit): ")
        if video_url.lower() == 'exit':
            return None
        # Validate URL format if necessary
        return video_url

def main():
    print_welcome_message()
    channel_ids = []
    

    while True:
        video_url = get_user_input()
        if video_url is None:
            break
        try:
            channel_id = get_channel_id(video_url)
            if channel_id:
                print(f"Channel ID: {channel_id}")
                channel_ids.append(channel_id)
            else:
                print("Channel ID not found.")
        except Exception as e:
            print(f"Error occurred: {e}")
    
    if channel_ids:
        print("\nCollected Channel IDs:", channel_ids)
        
        try:
            channel_data = dataProcess(channel_ids)
            print("\nChannel Data:")
            print(channel_data)
            
            # Ask user if they want to save the data
            choice = input("\nWould you like to save this data as a CSV file? (y/n): ").lower()
            if choice == 'y':
                filename = input("Enter filename for CSV export (default 'channel_data.csv'): ").strip()
                if not filename:
                    filename = 'channel_data.csv'
                export_to_csv(channel_data, filename)
            else:
                print("Data not saved.")
        except Exception as e:
            print(f"Error occurred while processing data: {e}")
    else:
        print("No channel IDs to process.")

if __name__ == "__main__":
    main()
