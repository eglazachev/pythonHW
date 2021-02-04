start_dist = float(input('Enter the distance to begin with: '))
goal_dist = float(input('Enter the goal distance: '))
marathon = 42.195
days = 1
curr_day_dist = start_dist
if start_dist < goal_dist:
    while curr_day_dist < goal_dist:
        curr_day_dist *= 1.1
        days += 1
    print('\nYou will reach your goal in ', days, ' days!\nGood luck!')
else:
    print('\nYou have already reached your goal')
curr_day_dist = start_dist
days = 1
while curr_day_dist < marathon:
    curr_day_dist *= 1.1
    days += 1
print('\nBy the way you can overcome marathon in ', days, ' days!\nThink beyond;)')
