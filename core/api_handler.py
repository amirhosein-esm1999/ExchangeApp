import requests
import pandas as pd

# Fetches the desired exchange rates from the ExchangeRate API
def fetch_graph_data():
    url = "https://v6.exchangerate-api.com/v6/dcf161b7bbad2f9b8b8859c4/latest/USD"
    desired_currencies = ["USD", "EUR", "GBP", "JPY", "INR", "AUD", "CNY"]

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()
        if data.get("result") == "success":
            filtered_data = {currency: data["conversion_rates"][currency] for currency in desired_currencies}
            return filtered_data
        print("API response was not successful.")
        return None

    except requests.exceptions.RequestException as error:
        print("error: ", error)
        return None

# Fetches the pair conversion rate between two currencies
def pair_conversion(source, target,amount):
    url = f"https://v6.exchangerate-api.com/v6/dcf161b7bbad2f9b8b8859c4/pair/{source}/{target}/{amount}"
    try:
        response = requests.get(url, timeout=15)
        data = response.json()
        response.raise_for_status()
        if data.get("result") == "success":
            return data.get("conversion_result")
        print("API response was not successful.")
        return None
    except requests.exceptions.RequestException as error:
        print("error: ", error)
        return None

# Converts the exchange rates dictionary to a DataFrame
def convert_to_dataframe(rates_dict):
    df = pd.DataFrame(list(rates_dict.items()), columns=["Currency", "ExchangeRate"])
    return df