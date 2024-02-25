import random
import time

people = ["Justin", "Josh", "Steph", "Troy"]
original_list = ["North Carolina", "New York", "Oregon", "Arizona", "Michigan", "Tennessee", "California", "Idaho", "Washington", "Colorado", "Wyoming", "Florida", "Montana", "California", "New York", "Tennessee", "Florida", "Oregon", "Washington", "North Carolina"]


class findLocation:
        def __init__(self):
                print ()
                self.original_list = original_list

        def Locate(self):
                thelist = []
                while len(thelist) < 12:
                        state_to_add = random.choice(self.original_list)
                        if state_to_add not in thelist:
                                thelist.append(state_to_add)
                print(thelist)
                #original_list = thelist.copy()
                for _p in people:
                        removelist = []
                        statesdontexist = False
                        while len(removelist) != 2 or statesdontexist:
                                states_to_remove = input("Which two states would {} like to remove?".format(_p))
                                print(states_to_remove)
                                removelist = states_to_remove.split(',')
                                removelist = [x.strip(' ') for x in removelist]
                                print(removelist)
                                if len(removelist) != 2:
                                        print("Please enter 2 states separated by a comma.")
                                for _i in removelist:
                                        if _i not in self.original_list:
                                                statesdontexist = True
                                                print("Sorry, {} does not exist in the list.".format(_i))
                                                break
                                        statesdontexist = False

                        for _i in removelist:
                                if _i in thelist:
                                        thelist.remove(_i.strip())

                print()
                print(thelist)
                print("And the winner is...")
                print("")
                time.sleep(5)
                print(random.choice(thelist))

myNewLocation = findLocation()
myNewLocation.Locate()
