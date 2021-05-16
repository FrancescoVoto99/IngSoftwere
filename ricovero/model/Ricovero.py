import time

class Ricovero():

    def __init__(self, finericovero):
        self.finericovero = finericovero

    def is_finericovero(self):
        timestamp = int(time.time())
        return timestamp > self.finericovero