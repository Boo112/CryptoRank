
def test_order(self, order: Order):
        return self.client.create_test_order(
            symbol=order.symbol,
            side=order.side,
            type=order.type,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=order.quantity,
            price=order.price
        )


def get_client(self):
        return self.client
# QUESTION: is this behavior expected?

