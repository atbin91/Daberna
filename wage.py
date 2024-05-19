#set kardan shart bazi
def set_wage():
    try:
        wage = int(input("enter your wage: "))
        return wage
    except Exception as r:
        print(f"{r}")
