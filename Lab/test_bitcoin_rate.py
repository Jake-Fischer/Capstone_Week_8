import unittest 
from unittest import TestCase
from unittest.mock import patch 

import bitcoin_rate

class TestBitcoinRate(TestCase):

    @patch('bitcoin_rate.get_response')
    def test_get_btc_to_usd(self, mock_btc_api):

        mock_btc_api.return_value = {"time":
        {"updated":"Oct 21, 2021 00:08:00 UTC","updatedISO":"2021-10-21T00:08:00+00:00","updateduk":"Oct 21, 2021 at 01:08 BST"},
        "disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
        "chartName":"Bitcoin",
        "bpi":{"USD":{"code":"USD","symbol":"&#36;","rate":"65,830.9050","description":"United States Dollar","rate_float":123.0},
        "GBP":{"code":"GBP","symbol":"&pound;","rate":"47,627.5406","description":"British Pound Sterling","rate_float":47627.5406},
        "EUR":{"code":"EUR","symbol":"&euro;","rate":"56,495.0952","description":"Euro","rate_float":56495.0952}}}

        expected_dollars = 1230.0
        # mock_response.side_effect = [example_api_response]

        actual_dollars = bitcoin_rate.get_btc_to_usd(10)
        expected = 1230

        self.assertEqual(expected, converted)
