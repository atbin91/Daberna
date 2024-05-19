from random import shuffle
from file_op import save

#karhaye asli bazi (adad ha , tanzim pool ha)
def play(u_wage, u_players):
    wage = u_wage
    players = u_players
    try:
        a = list(range(1, 101))
        #random kardan adad ha 
        shuffle(a)
        #
        
        #ghesmat asli bazi
        while len(a) > 0:
            number = a.pop(0)
            print(number)
            option = input()
            if option == "e" or option == "E":
                winner = input("who win?")
                try:
                    for player in players:
                        #ezafe shodan pool be barande
                        if player["name"] != winner:
                            player["money"] -= wage
                        #kam shodan pool digaran
                        elif player["name"] == winner:
                            player["money"] += (len(players) - 1) * wage
                            save()

                except Exception as e:
                    print(f"{e} happend, check winner name...")

                return players
    except Exception as w:
        print(f"{w}")
