monthes_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
           'September', 'October', 'November', 'December']
monthes_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
           9: 'September', 10: 'October', 11: 'November', 12: 'December'}
month_number = int(input('Enter the number of month: '))
print(monthes_list[month_number - 1])
print(monthes_dict.get(month_number))
