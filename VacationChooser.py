import random
import time

valid_states = [
         'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',
         'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
         'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
         'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
         'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
         'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
         'North Carolina', 'North Dakota', 'Ohio',
         'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island',
         'South  Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah',
         'Vermont', 'Virginia', 'Washington', 'West Virginia',
         'Wisconsin', 'Wyoming']

users = ["Troy", "Steph", "Justin", "Josh"]


class Vacation:

    def __init__(self):
        self.full_list = []

    def remove_from_list(self, states_to_remove):
        for state in states_to_remove:
            if state in self.full_list:
                self.full_list.remove(state)
            else:
                print(f"Cannot remove {state} from list.")

    def add_to_list(self, states_to_add):
        for state in states_to_add:
            if state in valid_states:
                self.full_list.append(state)
            else:
                print(f"Sorry.  No such state as {state}")

    def choose_random(self):
        return random.choice(self.full_list)

    def ask_user_for_states(self, str_to_print, num_states, remove=False):
        state_list = []
        num = 1
        print(str_to_print + "\n\n")
        if remove:
            check_states = self.full_list
            prt_str = "That state is not in the list.\n"
        else:
            check_states = valid_states
            prt_str = "Sorry.  Please enter a valid U.S. state.\n"

        while num <= num_states:
            state = input(f"Enter state #{num} ->\n")
            while state not in check_states:
                print(prt_str)
                state = input(f"Enter state #{num} ->\n")
            state_list.append(state)
            num += 1
        if remove:
            self.remove_from_list(state_list)
        else:
            self.add_to_list(state_list)

    def __str__(self):
        return self.choose_random()


vacation = Vacation()
for username in users:
    vacation.ask_user_for_states(f"Please enter 5 states to add for {username}.", 5)
for username in users:
    vacation.ask_user_for_states(f"Please enter 2 states to remove for {username}", 2, remove=True)

print("\nAnd the winner is...\n")
time.sleep(5)
print(vacation)
