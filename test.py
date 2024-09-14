text = "loonbalxballpoon"

balloon = {}
word ="balloon"
count = 0
for letter in text:
    if letter in balloon and letter in word:
        balloon[letter] += 1
    elif letter in word:
        balloon[letter] = 1
while True:
    for letter in word:
        if letter in balloon and balloon[letter] > 0:
            balloon[letter] -= 1
        else:
            print(count)
    count += 1
    print(balloon)