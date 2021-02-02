total_sec = int(input('Enter a quantity of seconds:'))
seconds = total_sec % 60
minutes = (total_sec // 60) % 60
hours = total_sec // 3600
print(hours, ':', minutes, ':', seconds)
