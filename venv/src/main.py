import pandas as pd
import yfinance as yf
from src.classes.data_fetching.fetch_data import dataFetch
from src.classes.calculations.data_calculations import  dataCalc
from src.classes.data_generation import data_generation as dg
from src.classes.report_class import Reports
if __name__ == '__main__':
    grabData = dataFetch
    grabCalc = dataCalc
    genData = dg.dataGenerator
    newReportClass = Reports(20, 0.2, 100, 30)
    FinReport = genData.generate_financial_report(grabData.fetch_financial_metrics("AAPL"), newReportClass.get_dividends())
    # print(grabData.fetch_and_preprocess_data("AAPL",'2023-12-25', '2024-01-01'))
    # grabCalc.calculate_wacc_unformatted(12000000, 60, 40, .21)
    # new_data = ["AAPL", '2023-12-25', '2024-01-01', grabCalc.calculate_wacc(12000000, 60, 40, .21)]
    print(FinReport)
    newReportClass.set_dividends(5)
    FinReport = genData.generate_financial_report(grabData.fetch_financial_metrics("AAPL"), newReportClass.get_dividends())
    print(FinReport)
