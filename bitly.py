#!/bin/python
import requests
import os
import argparse
from dotenv import load_dotenv


def get_user_info(token):
    url = "https://api-ssl.bitly.com/v4/user"
    headers = {"Authorization": token}
    response = requests.get(url, headers=headers)
    return response.json()["id"]
    

def shorten_link(long_url, token):
    headers = {"Authorization": token}
    url = "https://api-ssl.bitly.com/v4/bitlinks"
    body = {"long_url": long_url}
    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()
    return response.json()["id"]


def count_clicks(bitlink, token):
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary"
    headers = {"Authorization": token}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


def set_script_arguments():
    parser = argparse.ArgumentParser(description="Create short link or count\
                                clicks for short link")
    parser.add_argument("url", help="URL for bitly-link or your bitly-link", 
                        type=str)
    return parser.parse_args()


if __name__ == '__main__':
    arguments = set_script_arguments()
    load_dotenv()
    USER_TOKEN = os.getenv("BITLY_TOKEN")
    
    input_URL = arguments.url 
    if (input_URL.startswith("bit.ly")):
        try:
            print("Total clicks", count_clicks(input_URL, USER_TOKEN))
        except requests.HTTPError:
            print("Wrong URL")
    else:
        try:
            print(shorten_link(input_URL, USER_TOKEN))
        except requests.HTTPError:
            print("Wrong URL!")



  
