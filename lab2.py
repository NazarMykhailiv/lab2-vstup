while True:
    print('choose a or b: \n\t a)Sort words by alphabet \n\t b)Count the number of letters.\nEnter "stop" if you want to exit ')

    option = input()

    if option == 'stop':
        break

    words = input("Enter some text:")
    if option == 'a':
        sortedtext = (sorted(words.split(), key=str.lower))
        uniqueWords = set()
        for word in sortedtext:
            if word not in uniqueWords:
                uniqueWords.add(word)
                if len(word.strip()) > 2:
                    print(word)

    if option == 'b':

        symbols = dict()

        for i in str.lower(words):
            if i == ' ':
                continue

            if i in symbols:
                symbols[i] += 1
            else:
                symbols[i] = 1

        for character in symbols:
            print("Letter ", character, " number = ", symbols[character])
