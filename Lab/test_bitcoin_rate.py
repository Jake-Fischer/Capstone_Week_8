import unittest 
from unittest import TestCase
from unittest.mock import patch 

import bitcoin_rate

"""
This is confusing stuff for me, I did my best. I tried to structure it similar to test_exchange_rate.py because it seemed similar. 
I am unsure why the program runs and prompts the user for data when the tests are run. But it does do that.
"""

class TestBitcoinRate(TestCase):

    @patch('bitcoin_rate.get_bitcoin_exchange_rate')
    def test_get_bitcoin_exchange_rate(self, mock_rates):

        mock_rate = 5
        example_api_response = {"time":
        {"updated":"Oct 21, 2021 00:08:00 UTC","updatedISO":"2021-10-21T00:08:00+00:00","updateduk":"Oct 21, 2021 at 01:08 BST"},
        "disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
        "chartName":"Bitcoin",
        "bpi":{"USD":{"code":"USD","symbol":"&#36;","rate":"65,830.9050","description":"United States Dollar","rate_float":mock_rate},
        "GBP":{"code":"GBP","symbol":"&pound;","rate":"47,627.5406","description":"British Pound Sterling","rate_float":47627.5406},
        "EUR":{"code":"EUR","symbol":"&euro;","rate":"56,495.0952","description":"Euro","rate_float":56495.0952}}}
        
        mock_rates.side_effect = [ example_api_response ]
        dollar_amount = bitcoin_rate.calculate_value_in_USD(10, 5) # I think this is correct, but it seems strange that I am just feeding it 5 instead of having it parse the data.
        expected_dollars = 50
        self.assertEqual(expected_dollars, dollar_amount)
