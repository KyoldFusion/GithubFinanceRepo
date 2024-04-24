class dataGenerationService():
    def generateFinanceReportValues(dictionaryFinancials, dcf_valuation):
        listValues = []
        for k,v in dictionaryFinancials.items():
            listValues.append(v)
        listValues.append(dcf_valuation)
        return listValues

