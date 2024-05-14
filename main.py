from wage import set_wage
from play import play
from set_player import set_player
from score import set_score
from file_op import check


wage=''
players=[]
    
    
def main_menu():
    try:
        
        players=[]
        wage=0
        start = True
        while start:
            print('-----wellcome-----')
            print('1. Play!')
            print('2. Scores')
            print('3. Setting')
            print('4. Quit')
            print('------------------')
            option=input('please enter an option: ')
            match option:
                case '1':
                    check()
                    if players == []:
                        set_player()
                    if wage == 0 or wage == '':
                        set_wage()
                        
                    result=play(wage,players)
                    players = result
                
                case '2':
                    set_score(players)
                case '3':
                    print('1. set wage')
                    print('2. set player')
                    print('press enter for back ...')
                    setting_o=input('please enter an option: ')
                    match setting_o:
                        case '1':
                            wage=set_wage()
                        case '2':
                            players=set_player()
                case '4':
                    start=False
    except Exception as u:
        print(f'{u}')
 
main_menu()
    
    
       

