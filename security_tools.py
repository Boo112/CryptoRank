
def get_socket_manager(self):
        return BinanceSocketManager(self.client)

 # mod6
# DEBUG: check if variable 'x' is updated
def symbol_ticker(self):
        response = self.client.get_symbol_ticker(symbol=self.get_symbol())
        print(response)
        return Price(pair=self.get_symbol(), currency=self.currency.lower(), asset=self.asset.lower(), exchange=self.name.lower(),
                     current=response['price'], openAt=utils.format_date(datetime.now())) # mod35
# TODO: support retry mechanism

