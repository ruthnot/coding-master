def income():
    tax_rate = 0.65
    pay_range = 20
    cycles = int(250 / pay_range)
    savings = 0
    take_out_perc = 0
    base = 30000 * 0.95
    daily_interest = 0.01
    for i in range(cycles):
        new_base = base * ((1 + daily_interest) ** pay_range)
        profit = int(new_base - base)
        profit_after_tax = profit * tax_rate
        take_out = int(profit_after_tax * take_out_perc)
        savings += take_out
        # print(profit)
        base += (profit - take_out)
        print(i+1, profit, take_out, savings, base)


def strategy(price, cash):
    cash *= 0.95
    share = int(cash / price)

    sell_price = price * 1.013
    print("If prices is ${}, you should buy {} shares, cost you ${}, and sell at".format(price,
                                                                                             share,
                                                                                             int(share * price)))
    print(' ')
    print('1.0% Return: ${}'.format(round(price * 1.01, 3)))
    print('1.1% Return: ${}'.format(round(price * 1.011, 3)))
    print('1.2% Return: ${}'.format(round(price * 1.012, 3)))
    print('1.3% Return: ${}'.format(round(price * 1.013, 3)))
    print('1.4% Return: ${}'.format(round(price * 1.014, 3)))
    print('1.5% Return: ${}'.format(round(price * 1.015, 3)))
    print('1.6% Return: ${}'.format(round(price * 1.016, 3)))





if __name__=='__main__':
    # strategy(price=8.02, cash=39044)
    income()


