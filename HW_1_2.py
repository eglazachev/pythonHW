total_sec = int(input('Enter the quantity of seconds:'))
seconds = total_sec % 60
minutes = (total_sec // 60) % 60
hours = total_sec // 3600
print(hours, ':', minutes, ':', seconds)
