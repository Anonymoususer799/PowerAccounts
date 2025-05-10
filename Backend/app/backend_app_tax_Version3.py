from decimal import Decimal

class TaxCalculator:
    def __init__(self, tax_rate):
        self.tax_rate = Decimal(tax_rate)

    def calculate_tax(self, amount):
        tax_amount = (Decimal(amount) * self.tax_rate) / 100
        total_amount = Decimal(amount) + tax_amount
        return {
            'tax_amount': round(tax_amount, 2),
            'total_amount': round(total_amount, 2)
        }