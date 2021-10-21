import requests


def main():
    exchange_rate = get_bitcoin_exchange_rate()
    user_bitcoin = get_user_bitcoin()
    bitcoin_value_in_usd = calculate_value_in_USD(user_bitcoin, exchange_rate)
    display_results(user_bitcoin, bitcoin_value_in_usd)


def get_bitcoin_exchange_rate():
    """Gets the exchange rate and returns it"""
    coindesk_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(coindesk_url)
    data = response.json()
    dollars_exchange_rate = data['bpi']['USD']['rate_float']
    return dollars_exchange_rate


def get_user_bitcoin():
    """Asks the user for a number greater than 0 and then returns it"""
    while True:
        bitcoin = float(input('Enter number of bitcoins: '))
        if bitcoin > 0:
            return bitcoin
        else:
            print('Please enter an amount greater than 0')


def calculate_value_in_USD(bitcoin, exchange_rate):
    bitcoin_value_in_USD = bitcoin * exchange_rate
    return bitcoin_value_in_USD


def display_results(bitcoin, bitcoin_value_in_USD):
    print(f'{bitcoin} bitcoin is worth ${bitcoin_value_in_USD}')


main()