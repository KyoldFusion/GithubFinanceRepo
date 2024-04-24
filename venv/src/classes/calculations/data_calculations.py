import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense
from src.service.data_calculation_service import calculationServices
class dataCalc():

    def calculate_wacc(market_cap, total_debt, interest_expense, tax_rate):
        grabWacc = calculationServices.calculate_wacc_service(market_cap, total_debt, interest_expense, tax_rate)
        grabWacc = "Wacc: " + "{:.4f}".format(grabWacc)
        return grabWacc

    def calculate_wacc_unformatted(market_cap, total_debt, interest_expense, tax_rate):
        grabWacc = calculationServices.calculate_wacc_service(market_cap, total_debt, interest_expense, tax_rate)
        return grabWacc

    def calculate_dcf(latest_fcf, fcf_growth_rate, wacc, years=10):
        try:
            cash_flows = [latest_fcf * ((1 + fcf_growth_rate) ** min(i, 20)) for i in
                          range(1, years + 1)]  # Cap growth compounding
            terminal_value = cash_flows[-1] * (1 + 0.02) / (wacc - 0.02)
            discount_factors = [(1 / (1 + wacc)) ** i for i in range(1, years + 2)]
            dcf_valuation = sum(cf * df for cf, df in zip(cash_flows, discount_factors[:-1])) + terminal_value * \
                            discount_factors[-1]
        except OverflowError:
            print("Overflow error encountered in DCF calculation")
            dcf_valuation = np.nan
        return dcf_valuation