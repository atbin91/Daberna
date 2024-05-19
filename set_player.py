import json

file_name = "player.txt"

#gereftan etelaat bazi konan va zakhire anan(pool , tedad anha , esmeshan)
def set_player():

    players = []
    t = int(input("'pleae enter the tedad player: "))
    money = int(input(f"please enter player's money: "))
    for i in range(0, t):
        name = input(f"please enter player's name: ")
        p = {"name": name, "money": money}

        players.append(p)
        print(players)
    #zakhire etelaat
    with open(file_name, "w") as f:
        json.dump(players, f)
    #khandan etelaat
    with open(file_name, "r") as ff:
        players1 = json.loads(ff.read())

    return players
