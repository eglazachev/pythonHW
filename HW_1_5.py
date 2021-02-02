earnings = float(input('Enter the amount of total earnings: '))
costs = float(input('Enter the amount of total costs: '))
if earnings > costs:
    print('\nCongratulation, your income is', (earnings - costs), '.')
    print('Profitability is ', round((earnings - costs)/earnings, 2), '\nKeep forward!')
    staff = int(input('\nEnter the number of your workers: '))
    print('So you have ', round((earnings - costs)/staff, 2), ' as income per worker')
elif earnings == costs:
    print('\nYour doings are ok, you now have balanced costs and earnings.\nKeep working!')
else:
    print('\nYou lose your money. Your losses are: ', (costs - earnings), '\nTry your best!')
