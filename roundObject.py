class Round:
    active = True

    def __init__(self, brewer, initial_orders={}):
        self.brewer = brewer
        self.orders = initial_orders

    def add_order(self, person, drink):
        self.orders.update({person: drink})

    def remove_order(self, person):
        self.orders.pop(person)

    def clear(self):
        self.orders.clear()

    def finish_round(self):
        self.active = False

newRound = Round("Eduardo")