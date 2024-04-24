class Reports:
    def __init__(self, dividends, wacc, fcf, dcf):
        self._dividends = dividends
        self._wacc = wacc
        self._fcf = fcf
        self._dcf = dcf


    def get_dividends(self):
        return self._dividends

    def set_dividends(self, new_dividends):
        self._dividends = new_dividends
