import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense
from src.service.data_generation_service import dataGenerationService as dgs
class dataGenerator():

    dataGen = dgs

    def build_and_train_lstm_model(data):
        scaler = MinMaxScaler(feature_range=(0, 1))
        scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1, 1))
        X, y = [], scaled_data[1:]
        for i in range(len(scaled_data) - 1):
            X.append(scaled_data[i:i + 1, 0])
        X, y = np.array(X), np.array(y)

        model = Sequential([
            Input(shape=(1, 1)),  # Define the input shape directly here
            LSTM(50, return_sequences=True),
            Dropout(0.2),
            LSTM(50),
            Dropout(0.2),
            Dense(1)
        ])
        model.compile(optimizer='adam', loss='mean_squared_error')
        model.fit(X, y, epochs=20, batch_size=32)
        return model

    def generate_financial_report(financial_metrics, dcf_valuation):
        report = {}
        keys = ["dividends", "FCF Growth Rate", "WACC", "WAC_Percent"]
        grabFinValues = dgs.generateFinanceReportValues(financial_metrics, dcf_valuation)
        for i in range(0, len(keys)):
            report[keys[i]] = grabFinValues[i]
        return report
        # report = f"Financial Analysis Report:\n"
        # report += f"DCF Valuation: ${dcf_valuation:.2f}\n"
        # report += f"WACC: {financial_metrics['wacc']:.2%}\n"
        # report += f"FCF Growth Rate: {financial_metrics['fcf_growth_rate']:.2%}\n"
        # report += f"Total Dividends (Last 5 Years): ${financial_metrics['dividend_rate']}\n"
