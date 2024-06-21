def purchase(price, money_available):
    leftover_money = money_available - price
    if (leftover_money < 0):
        raise Exception("not enough money")
    else:
        return leftover_money
