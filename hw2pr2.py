def calcualte_change(amount):

    change=100-amount

    if change==0:
        print("no change")
        return
    elif change==1:
        print("Your change is:",change,"cent")
    else:
        print("Your change is:",change,"cents")

    quarters=0
    dimes=0
    nickels=0
    pennies=0

    quarters = change // 25
    change %= 25

    dimes = change // 10
    change %= 10

    nickels = change // 5
    change %= 5

    pennies=change//1
    change%=1
    
    if quarters > 0:
        print(quarters,'quarter' if quarters == 1 else 'quarters')
    if dimes > 0:
        print(dimes, 'dime' if dimes == 1 else 'dimes')
    if nickels > 0:
        print(nickels,'nickel' if nickels == 1 else 'nickels')
    if pennies > 0:
        print(pennies,'penny' if pennies == 1 else 'pennies')
    print()
            
            

#if __name__ == '__main__':
for amount in [0, 4, 5, 10, 13, 25, 27, 30, 55, 73, 99, 100]:
    calcualte_change(amount)
print() 