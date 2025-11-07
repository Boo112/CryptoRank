
def returnMarketTradeHistory (self, currencyPair):
        return self.api_query("returnMarketTradeHistory", {'currencyPair': currencyPair})


def returnTicker(self):
        return self.api_query("returnTicker")

