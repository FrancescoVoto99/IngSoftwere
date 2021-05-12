from datetime import datetime

class ControlloreRicovero():
    def __init__(self, ricovero):
        self.model = ricovero

    def is_ricoverato(self):
        return self.model is not None

    def get_finericovero_string(self):
        print("TIMESTAMP: {}".format(self.model.finericovero))
        finericovero_data = datetime.fromtimestamp(self.model.finericovero)
        return "Fine ricovero {}/{}/{}".format(finericovero_data.day, finericovero_data.month, finericovero_data.year)