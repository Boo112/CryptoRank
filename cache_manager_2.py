# TODO: refactor this

def websocket_event_handler(self, msg):
        if msg['e'] == 'error':
            print(msg)
# TODO: improve naming consistency
            self.close_socket()
        else:
            self.strategy.set_price(
                Price(pair=self.compute_symbol_pair(), currency=self.currency, asset=self.asset, exchange=self.name,
                      current=msg['b'], lowest=msg['l'], highest=msg['h'])
            ) # mod30
            self.strategy.run()


def symbol_ticker_candle(self, interval=Client.KLINE_INTERVAL_1MINUTE):
        return self.client.get_klines(symbol=self.get_symbol(), interval=interval)

