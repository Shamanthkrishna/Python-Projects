import psutil
from pynotifier import Notification
import time
import datetime
import os

def send_notification_with_retry(notification, retries=3, delay=2):
    for _ in range(retries):
        try:
            notification.send()
            print("Notification sent successfully.")
            return
        except Exception as e:
            print(f"Notification failed: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
    print("Notification failed after multiple attempts.")

def log_battery_status(percent, plugged):
    """Log battery status to a text file."""
    # Determine the path of the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_file_path = os.path.join(script_dir, 'battery_log.txt')
    
    with open(log_file_path, 'a') as file:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f'{timestamp} - Battery: {percent}%, Plugged In: {plugged}\n')
    print(f"Battery status logged to {log_file_path}")

# Fixed settings
THRESHOLD_PERCENT = 30
NOTIFICATION_DURATION = 5

# Check battery status
battery = psutil.sensors_battery()

if battery is None:
    print("Battery information not available.")
else:
    plugged = battery.power_plugged
    percent = battery.percent
    
    # Print battery info
    print(f'Battery Percentage: {percent}%')
    print(f'Power Plugged In: {plugged}')

    # Log battery status
    log_battery_status(percent, plugged)

    if percent <= THRESHOLD_PERCENT and not plugged:
        # Send notification
        notification = Notification(
            title="Battery Low",
            description=f"{percent}% Battery remaining!",
            duration=NOTIFICATION_DURATION
        )
        send_notification_with_retry(notification)
