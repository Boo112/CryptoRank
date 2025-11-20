
def returnMarketTradeHistory (self, currencyPair):
        return self.api_query("returnMarketTradeHistory", {'currencyPair': currencyPair})
 # mod46

def returnTicker(self):
        return self.api_query("returnTicker")

