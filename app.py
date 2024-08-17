from flask import Flask, jsonify, request
import requests
from threading import Lock

app = Flask(_name_)
WINDOW_SIZE = 10
lock = Lock()
numbers_window = []

API_URLS = {
    'p': "http://20.244.56.144/test/primes",    
    'fibo': "http://20.244.56.144/test/fibo",    
    'e': "http://20.244.56.144/test/even",     
    'r': "http://20.244.56.144/test/rand"       
}

def add_number_to_window(number):
    with lock:
        if num not in numbers_window:
            if len(numbers_window) >= WINDOW_SIZE:
                numbers_window.pop(0) 
            numbers_window.append(num)

def calculate_average():
    if len(numbers_window) == 0:
        return 0.00
    return round(sum(numbers_window) / len(numbers_window), 2)

def fetch_numbers_from_api(api_url):
    try:
        response = requests.get(api_url, timeout=0.5)
        if response.status_code == 200:
            data = response.json()
            return data.get('numbers', [])
    except (requests.Timeout, requests.RequestException):
        return []  
    return []

@app.route("/numbers/<type_id>", methods=["GET"])
def get_numbers(type_id):
    if type_id not in API_URLS:
        return jsonify({"error": "Invalid number type"}), 400
    api_url = API_URLS[type_id]
    fetched_numbers = fetch_numbers_from_api(api_url)
    
    if not fetched_numbers:
        return jsonify({"error": "No numbers retrieved or API request failed"}), 500

    before_numbers = list(numbers_window)

    for number in fetched_numbers:
        add_number_to_window(number)

    after_numbers = list(numbers_window)

    average = calculate_average()

    return jsonify({
        "windowPrevState": before_numbers,
        "windowCurrState": after_numbers,
        "numbers": fetched_numbers,
        "avg": "{:.2f}".format(average)
    }), 200

if _name_ == "_main_":
    app.run(port=9876)