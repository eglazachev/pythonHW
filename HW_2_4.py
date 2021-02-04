user_words = input('Type here some words:\n')
i = 1
for word in user_words.split():
    print(i, word[:10])
    i += 1
