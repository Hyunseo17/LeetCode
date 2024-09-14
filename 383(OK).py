import sys

ransomNote = "aa"
magazine = "aab"

letters = {}

for i in magazine:
    if i not in letters:
        letters[i] = 1
    else:
        letters[i] += 1

for i in ransomNote:
    if i in letters and letters[i] > 0:
        letters[i] -= 1
    else:
        print(False)
        sys.exit()

print(True)