import requests


def fetch_data():
    return requests.get('https://random-data-api.com/api/bank/random_bank')
