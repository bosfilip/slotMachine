import random

def spinrow():

    listOutcomes = ["🍒", "🍉", "🍌", "🔔", "⭐"]

    outcome = []
    for symbol in range(3):
        outcome.append(random.choice(listOutcomes))
    return outcome

def showrow(row):
    print(" | ".join(row))

def payout(bet, row):
    if row[0] == "🍒" and row[0] == row[1] == row[2]:
        nBet = bet * 2
        return nBet
    elif row[0] == "🍉" and row[0] == row[1] == row[2]:
        nBet = bet * 3
        return nBet
    elif row[0] == "🍌" and row[0] == row[1] == row[2]:
        nBet * 5
        return nBet
    elif row[0] == "🔔" and row[0] == row[1] == row[2]:
        nBet = bet * 10
        return nBet
    elif row[0] == "⭐" and row[0] == row[1] == row[2] :
        nBet = bet * 20
        return nBet
    else:
        return 0

def main():
    print("WELLCOME TO SPIN MACHINE")
    print("Possible outcomes: 🍒 🍉 🍌 🔔 ⭐")
    balance = 100

    while balance > 0:

        print(f"Your current balance is {balance}")

        bet = input("Enter your bet: ")

        if not bet.isdigit():
            print("Bet must be a digit")
            continue

        bet = int(bet)

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        if bet > balance:
            print("Insufficient founds")
            continue

        balance -= bet

        row = spinrow()
        showrow(row)
        p = payout(bet, row)
        balance += p
main()