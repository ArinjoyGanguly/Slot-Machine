import random
def spin_row():
    s=['🍒','🍉','🪙','🎈','🔔']
    r=[]
    for _ in range(3):
        r.append(random.choice(s))
    return r
def print_row(x):
    return " | ".join(x)
    
def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='🍒':
            pay=bet*2
        elif row[0]=='🍉':
            pay=bet*3
        elif row[0]=='🪙':
            pay=bet*5
        elif row[0]=='🎈':
            pay=bet*8
        elif row[0]=='🔔':
            pay=bet*10
        return pay
    return 0

def main():
    print("*************************")
    print("Welcome to slot machine")
    print("Symbols: 🍒🍉🪙 🎈🔔")
    print("*************************")
    balance=100
    print(f"Your balance={balance}$")
    while True:
        bet=input("Enter bet amount: ")
        if not bet.isdigit():
            print("Enter a proper number ")
            continue
        bet=int(bet)
        if bet<0:
            print("Enter a number greater than 0: ")
            continue
        if bet > balance:
            print("You cannot bet more than your current balance.")
            continue
        balance-=bet
        x=spin_row()
        print(print_row(x))
        payout=get_payout(x,bet)
        if payout>0:
            print(f"Your current win: {payout}$")
            balance+=payout
        else:
            print("Sorry! You have lost this round ")
        print(f"Your current balance={balance}$")
        a=input("Do you want to play another round: Y/N ").upper()
        if(a!="Y"):
            break
    print("*************************")
    print("GAME OVER 👾")
    print("*************************")

if __name__=='__main__':
    main()