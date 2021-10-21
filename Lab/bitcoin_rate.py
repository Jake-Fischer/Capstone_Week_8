import requests


def main():
    # json_data = get_response()
    # exchange_rate = get_exchange_rate(json_data)
    exchange_rate = get_btc_to_usd()
    user_bitcoin = get_user_bitcoin()
    bitcoin_value_in_usd = calculate_value_in_USD(user_bitcoin, exchange_rate)
    display_results(user_bitcoin, bitcoin_value_in_usd)


def get_btc_to_usd():
    data = get_response()
    rate = get_exchange_rate(data)
    return rate

def get_response():
    coindesk_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(coindesk_url)
    return response.json()


def get_exchange_rate(json_data):
    dollars_exchange_rate = json_data['bpi']['USD']['rate_float']
    return dollars_exchange_rate


def get_user_bitcoin():
    bitcoin = float(input('Enter number of bitcoins: '))
    return bitcoin


def calculate_value_in_USD(bitcoin, exchange_rate):
    bitcoin_value_in_USD = bitcoin * exchange_rate
    return bitcoin_value_in_USD


def display_results(bitcoin, bitcoin_value_in_USD):
    print(f'{bitcoin} bitcoin is worth ${bitcoin_value_in_USD}')


main()