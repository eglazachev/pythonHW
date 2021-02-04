ratings = [7, 5, 3, 3, 2]
inserted_num = int(input('Type a natural number: '))
i = 1
if (inserted_num > ratings[0]) or len(ratings) == 0:
    ratings.insert(0, inserted_num)
elif inserted_num < ratings[-1]:
    ratings.append(inserted_num)
else:
    while i < len(ratings):
        if (ratings[i-1] >= inserted_num) and (inserted_num > ratings[i]):
            ratings.insert(i, inserted_num)
            break
        i += 1
print(ratings)

