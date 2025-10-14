#!/bin/env python
import requests
from urllib import request as urllib_request
import http.client

def fetch_with_requests(url):
    try:
        response = requests.get(url)
        return response.status_code, response.text
    except requests.RequestException as e:
        return None, f"Requests error: {e}"

def fetch_with_urllib(url):
    try:
        with urllib_request.urlopen(url) as response:
            html = response.read().decode()
            return response.getcode(), html
    except Exception as e:
        return None, f"Urllib error: {e}"

def fetch_with_httpclient(url):
    try:
        # Extract host and path
        if url.startswith("https://"):
            url = url[8:]
        elif url.startswith("http://"):
            url = url[7:]
        host, _, path = url.partition("/")
        path = "/" + path
        conn = http.client.HTTPSConnection(host)
        conn.request("GET", path)
        res = conn.getresponse()
        data = res.read().decode()
        return res.status, data
    except Exception as e:
        return None, f"http.client error: {e}"

def save_output(status_code, text, filename):
    with open(filename, "w") as file:
        file.write(f"Status Code: {status_code}\n")
        file.write(f"Response snippet: {text[:200]}...\n")  # first 200 chars

def main():
    url = input("Enter URL (e.g., https://example.com): ").strip()
    print("Select method to fetch URL:")
    print("1: requests")
    print("2: urllib")
    print("3: http.client")
    choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        status, text = fetch_with_requests(url)
        filename = "output_requests.txt"
    elif choice == "2":
        status, text = fetch_with_urllib(url)
        filename = "output_urllib.txt"
    elif choice == "3":
        status, text = fetch_with_httpclient(url)
        filename = "output_httpclient.txt"
    else:
        print("Invalid choice!")
        return

    if status is None:
        print(f"Error: {text}")
    else:
        print(f"Status Code: {status}")
        save_output(status, text, filename)
        print(f"Output saved to {filename}")

if __name__ == "__main__":
    main()
