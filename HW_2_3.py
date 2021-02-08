monthes_list = ['Winter', 'Winter', 'Spring', 'Spring', 'Spring', 'Summer', 'Summer', 'Summer',
           'Autumn', 'Autumn', 'Autumn', 'Winter']
monthes_dict = {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring', 6: 'Summer', 7: 'Summer', 8: 'Summer',
           9: 'Autumn', 10: 'Autumn', 11: 'Autumn', 12: 'Winter'}
month_number = int(input('Enter the number of month: '))
print(monthes_list[month_number - 1])
print(monthes_dict.get(month_number))
