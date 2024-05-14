from main import main_menu
import json
import os.path



file_name="save_game.dll"

def save(players,wage):
    try:
        tmp_players={"players":players,"wage":wage}
        with open(file_name,"wt") as f:
            json.dump(tmp_players,f)
    except Exception as e:
        print(f'khata dar zakhire etelaat')
        
def load():
    try:
        with open(file_name,"rt") as f:
            tmp_players=json.load(f)
        yield(list(tmp_players["players"]))
        yield(tmp_players["wage"])
    except Exception:
        return False

def check():
    return os.path.exists(file_name)
        
         
       
