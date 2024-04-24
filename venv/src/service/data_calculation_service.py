

class calculationServices():

    def calculate_wacc_service(market_cap, total_debt, interest_expense, tax_rate):
        cost_of_debt = interest_expense / total_debt if total_debt > 0 else 0.04
        cost_of_equity = 0.08
        equity_ratio = market_cap / (market_cap + total_debt)
        debt_ratio = total_debt / (market_cap + total_debt)
        wacc = (cost_of_equity * equity_ratio) + (cost_of_debt * debt_ratio * (1 - tax_rate))
        return wacc