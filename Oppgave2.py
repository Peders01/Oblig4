import random

kortstokken =[
                {"Spar 2": 2}, {"Spar 3": 3}, {"Spar 4": 4}, {"Spar 5": 5}, {"Spar 6": 6},
                {"Spar 7": 7}, {"Spar 8": 8}, {"Spar 9": 9}, {"Spar 10": 10},
                {"Spar Knekt": 10}, {"Spar Dame": 10}, {"Spar Konge": 10}, {"Spar Ess": 11},

                {"Hjerter 2": 2}, {"Hjerter 3": 3}, {"Hjerter 4": 4}, {"Hjerter 5": 5}, {"Hjerter 6": 6},
                {"Hjerter 7": 7}, {"Hjerter 8": 8}, {"Hjerter 9": 9}, {"Hjerter 10": 10},
                {"Hjerter Knekt": 10}, {"Hjerter Dame": 10}, {"Hjerter Konge": 10}, {"Hjerter Ess": 11},

                {"Kløver 2": 2}, {"Kløver 3": 3}, {"Kløver 4": 4}, {"Kløver 5": 5}, {"Kløver 6": 6},
                {"Kløver 7": 7}, {"Kløver 8": 8}, {"Kløver 9": 9}, {"Kløver 10": 10},
                {"Kløver Knekt": 10}, {"Kløver Dame": 10}, {"Kløver Konge": 10}, {"Kløver Ess": 11},

                {"Ruter 2": 2}, {"Ruter 3": 3}, {"Ruter 4": 4}, {"Ruter 5": 5}, {"Ruter 6": 6},
                {"Ruter 7": 7}, {"Ruter 8": 8}, {"Ruter 9": 9}, {"Ruter 10": 10},
                {"Ruter Knekt": 10}, {"Ruter Dame": 10}, {"Ruter Konge": 10}, {"Ruter Ess": 11}
]

def get_card():
    kortet = random.choice(kortstokken)
    for key, value in kortet.items():
        key
    return key

















# class kort:
    # def __init__(self, slag, kortnr):
        # self.slag = slag
        # self.kortnr = kortnr


# class kortstokk:
    # def __init__(self):
        # self.slag = ["Spar", "Ruter", "Kløver", "Hjerter"]
        # self.kortnr = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Knekt", "Dame", "Konge", "Ess"]
        # self.kortet = kortet

# class spiller:
    # def __init__(self):

        # for kort in range(1, 52):
            # if kort <= 13:
                # kort = spar
                # spar = [{"slag": "Spar", "navn": 2},
                       # {"slag": "Spar", "navn": 3},
                       # {"slag": "Spar", "navn": 4},
                       # {"slag": "Spar", "navn": 5},
                       # {"slag": "Spar", "navn": 6},
                       # {"slag": "Spar", "navn": 7},
                       # {"slag": "Spar", "navn": 8},
                       # {"slag": "Spar", "navn": 9},
                       # {"slag": "Spar", "navn": 10},
                       # {"slag": "Spar", "navn": "Knekt"},
                       # {"slag": "Spar", "navn": "Dame"},
                       # {"slag": "Spar", "navn": "Konge"},
                       # {"slag": "Spar", "navn": "Ess"}
                       # ]
            # if 14 <= kort <= 26:
               # kort = "Hjerter"

           # if 27 <= kort <= 39:
               # kort = "Ruter"

           # if 40 <= kort <= 52:
               # kort = "Kløver"

#Dette er klassen kortstokk
#liste med alle kort

#for kort in range(52):
    #if kort <= 12:
        # spar
        #liste[kort] = "Spar ess"