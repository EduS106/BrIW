from source.app import number_cleaner, name_cleaner
class Round:
    active = True
    orders = {}
    # team must be stored in a teams file/database
    def __init__(self, brewer, preferences={}, team=[]):
        self.brewer = brewer
        self.preferences = preferences
        self.team = team
        self.opening_message = f"Welcome, {brewer}, you have started a new round!"

    def welcome(self):
        print(self.opening_message)

    def add_order(self, person, drink):
        self.orders.update({person: drink})

    def _remove_order(self, person):
        self.orders.pop(person)

    def _clear_orders(self):
        self.orders.clear()

    def close_round(self):
        self.active = False

def start_rounds():
    brewer = input("What is your name?\nName: ")
    newRound = Round(brewer)
    newRound.welcome()
    menu = f'''What would you like to do? Choose from the following options:
    
[1] Add order
[2] Add team mate
[3] Add '''


start_rounds()