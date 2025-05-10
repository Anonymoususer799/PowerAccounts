import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

class FinancialReports:
    def __init__(self, transactions):
        self.transactions = pd.DataFrame(transactions)

    def generate_profit_and_loss(self, start_date, end_date):
        filtered_data = self.transactions[
            (self.transactions['date'] >= start_date) & (self.transactions['date'] <= end_date)
        ]
        income = filtered_data[filtered_data['type'] == 'Income']['amount'].sum()
        expenses = filtered_data[filtered_data['type'] == 'Expense']['amount'].sum()
        profit = income - expenses

        return pd.DataFrame({
            'Category': ['Income', 'Expenses', 'Profit'],
            'Amount': [income, expenses, profit]
        })