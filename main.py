from wage import set_wage
from play import play
from set_player import set_player
from score import set_score
from file_op import check
from file_op import delete_save


wage = ""
players = []

#safheye asliye ejraeie bazi
def main_menu():
    try:

        players = []
        wage = 0
        start = True
        while start:
            print("-----wellcome-----")
            print("1. Play!")
            print("2. Scores")
            print("3. Setting")
            print("4. Quit")
            print("------------------")
            option = input("please enter an option: ")
            match option:
                case "1":
                    check()
                    if players == []:
                        set_player()
                    if wage == 0 or wage == "":
                        set_wage()

                    result = play(wage, players)
                    players = result

                case "2":
                    set_score(players)
                case "3":
                    print("1. delete all data")
                    print("2. set players")
                    print("3. set wage")
                    print("press enter for back ...")
                    setting_o = input("please enter an option: ")
                    match setting_o:
                        #pak kardan file
                        case "1":
                            players = []
                            wage = 0
                            delete_save()
                        #set kardan basikonan
                        case "2":
                            players = set_player()
                        #set kardan shart bazi
                        case "3":
                            wage = set_wage()

                case "4":
                    start = False
    except Exception as u:
        print(f"{u}")


main_menu()
