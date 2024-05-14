import json

file_name = "player.txt"


def set_player():

    players = []
    t = int(input("'pleae enter the tedad player: "))
    money = int(input(f"please enter player's money: "))
    for i in range(0, t):
        name = input(f"please enter player's name: ")
        p = {"name": name, "money": money}

        players.append(p)
    with open(file_name, "w") as f:
        json.dump(players, f)

    with open(file_name, "r") as ff:
        players1 = json.loads(ff.read())

    return players
