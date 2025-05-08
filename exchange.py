import requests

def get_eur_to_usd():

    url = "https://v6.exchangerate-api.com/v6/3186638126cd3cac3c3fcee1/latest/USD"

    response = requests.get(url)
    exchange_data = response.json()

    # print(exchange_data)
    conversion_rates = exchange_data['conversion_rates']
    # print(conversion_rates)
    usd = conversion_rates['USD']
    euro = conversion_rates['EUR']


    # Exchange rate: 1 USD = 0.8827 EUR
    usd_to_eur = euro

    # Calculate the reversed rate: 1 EUR = ? USD
    eur_to_usd = 1 / usd_to_eur

    # Ask the user to enter an amount in euros
    euro_input = input("Enter the amount in EUR: ")

    # Convert the input to a float number
    euros = float(euro_input)

    # Calculate how many dollars
    dollars = euros * eur_to_usd

    # Show the result
    print(f"{euros:.2f} EUR is equal to {dollars:.2f} USD (1 EUR = {eur_to_usd:.4f} USD)")

get_eur_to_usd()