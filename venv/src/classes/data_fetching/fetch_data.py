import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense

class dataFetch():

    def fetch_financial_metrics(symbol):
        stock = yf.Ticker(symbol)
        cash_flow = stock.cashflow.transpose().get("Free Cash Flow", pd.Series()).dropna()

        if len(cash_flow) > 1 and (cash_flow > 0).all():
            years = cash_flow.index.year.astype(float)
            values = cash_flow.values.astype(float)
            log_years = np.log(years)
            log_values = np.log(values)
            rates = np.polyfit(log_years, log_values, 1)
            fcf_growth_rate = np.exp(rates[0]) - 1
            latest_fcf = cash_flow.iloc[-1]
        else:
            fcf_growth_rate = np.nan
            latest_fcf = np.nan

        # Fetch and sum dividends
        end_year = pd.to_datetime('today').year
        start_year = end_year - 5
        dividends = stock.dividends.loc[f'{start_year}':f'{end_year}'].sum()

        return {
            'dividend_rate': round(dividends, 4),
            'fcf_growth_rate': "{:.4f}".format(fcf_growth_rate),
            'latest_fcf': "{:.4f}".format(latest_fcf)
        }

    def fetch_and_preprocess_data(symbol, start_date, end_date):
        data = yf.download(symbol, start=start_date, end=end_date)
        data.ffill(inplace=True)  # Forward fill to handle missing values
        return data