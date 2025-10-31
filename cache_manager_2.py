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


def order(self, order: Order):
        return self.client.create_order(
            symbol=order.symbol,
            side=order.side,
            type=order.type,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=order.quantity,
            price=order.price
        )


def __init__(self, key: str, secret: str):
        super().__init__(key, secret)


def get_socket_manager(self):
        return BinanceSocketManager(self.client)


def randomise_dictionary_inputs(strategy_dictionary_local):
    strategy_dictionary_local['ml_mode'] = choice(['adaboost', 'randomforest', 'gradientboosting', 'extratreesfitting']) #'svm'
    strategy_dictionary_local['regression_mode'] = choice(['regression', 'classification'])
    strategy_dictionary_local['preprocessing'] = choice(['PCA', 'FastICA', 'None'])
    return strategy_dictionary_local


def random_search_iteration(strategy_dictionary_local):
    strategy_dictionary_local = randomise_dictionary_inputs(strategy_dictionary_local)


def underlined_output(string):
    print string
    print '----------------------'
    print '\n'

# TODO: refactor this
