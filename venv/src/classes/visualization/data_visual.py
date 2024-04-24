import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense


class dataVisual():

    def visualize_data(data):
        plt.figure(figsize=(12, 6))
        plt.plot(data['Close'], label='Close Price')
        plt.title('Stock Prices Over Time')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()