from app.source.input_cleaner import number_cleaner


class Round:
    active = True
    orders = {}
    round_id = 0
    # team must be stored in a teams file/database

    def __init__(self, brewer, brewer_id, preferences={}, team=[]):
        self.brewer = brewer
        self.brewer_id = brewer_id
        self.preferences = preferences
        self.team = team
        self.opening_message = f"Welcome, {brewer}, you have started a new round!"

    def welcome(self, ids, drinks_dict):
        print(self.opening_message, "\n")
        drink_chosen = input("What drink would you like?\nDrink Number: ")
        drink_chosen = number_cleaner(drink_chosen)

        if len(drink_chosen) == 1:

            drink_index = drink_chosen[0] - 1

            if drink_index < len(ids) and drink_index != -1:
                drink_id = ids[drink_index]
                return drink_id
            else:
                user_exit = input('''Please make sure your name is on the list, please exit and add it if it is not.

Press ENTER to try again or type X to exit: ''')
                if user_exit.upper() == "X":
                    return 0
                else:
                    return -1

        else:
            user_exit = input('''Please only enter one number. Do not include words or special characters (!@£$%%^&*).

Press ENTER to try again or type X to exit: ''')
            if user_exit.upper() == "X":
                return 0
            else:
                return -1

    def add_team_member(self):
        pass

    def remove_team_member(self):
        pass

    def add_order(self, person_id, drink_id):
        self.orders.update({person_id: drink_id})

    def remove_order(self, person_id):
        self.orders.pop(person_id)

    def clear_orders(self):
        self.orders.clear()

    def close_round(self):
        self.active = False
        last_order = self.orders.copy()
        self.clear_orders()
        return last_order


#test_rounds()
