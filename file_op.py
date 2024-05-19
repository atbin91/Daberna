
import json
import os.path


file_name = "save.json"

#baraye save kardan etelaat bazikonan(pool , esm,shart)
def save(players, wage):
    try:
        tmp_players = {"players": players, "wage": wage}
        with open(file_name, "w") as f:
            json.dump(tmp_players, f)
    except Exception as e:
        print(f"khata dar zakhire etelaat")
        
#baraye avardan etelaat zakhireh shodeh
def load():
    try:
        #khandan eteelaat az file 
        with open(file_name, "r") as f:
            tmp_players = json.load(f)
        #dadan etelat bazikonan
        yield (list(tmp_players["players"]))
        #dadan shart
        yield (tmp_players["wage"])
    except Exception:
        return False

#barresi vojod dashtan yek file
def check():
    return os.path.exists(file_name)

#pak kardan file ha
def delete_save():
    try:
        os.remove(file_name)
    except Exception as e:
        print("Error happened"+ e.__str__)