import requests
from decimal import Decimal

class CurrencyConverter:
    API_URL = "https://api.currencyfreaks.com/latest"
    API_KEY = "your_api_key_here"

    def __init__(self):
        self.base_currency = "USD"

    def fetch_exchange_rates(self):
        try:
            response = requests.get(f"{self.API_URL}?apikey={self.API_KEY}&base={self.base_currency}")
            if response.status_code == 200:
                data = response.json()
                return data.get('rates', {})
            else:
                return {"error": "Failed to fetch exchange rates."}
        except Exception as e:
            return {"error": str(e)}

    def convert_currency(self, amount, from_currency, to_currency):
        rates = self.fetch_exchange_rates()
        if "error" in rates:
            return {"error": rates["error"]}

        if from_currency not in rates or to_currency not in rates:
            return {"error": "Currency not supported."}

        from_rate = Decimal(rates[from_currency])
        to_rate = Decimal(rates[to_currency])
        converted_amount = (Decimal(amount) / from_rate) * to_rate
        return round(converted_amount, 2)