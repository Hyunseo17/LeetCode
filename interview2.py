def solution(words):
    words = [word.lower() for word in words]
    suffix_map = {}
    count = 0
    
    for word in words:
        reversed_word = word[::-1]
        
        # Check if any suffix of the current word is in the map
        for i in range(len(reversed_word)):
            if reversed_word[i:] in suffix_map:
                count += 1
                break
        
        # Store all suffixes of the reversed word in the map
        for i in range(len(reversed_word)):
            suffix_map[reversed_word[i:]] = True
    return count


words = ["back", 
 "backdoor", 
 "gammon", 
 "backgammon", 
 "comeback", 
 "come", 
 "door"]
solution(words)

"""
Given an array of strings words, find the number of pairs where either the strings are equal or one string ends with another. In other words, find the number of such pairs i, j (0 ≤ i < j < words.length) that words[i] is a suffix of words[j], or words[j] is a suffix of words[i].

Example

For words = ["back", "backdoor", "gammon", "backgammon", "comeback", "come", "door"], the output should be solution(words) = 3.

The relevant pairs are:
1. words[0] = "back" and words[4] = "comeback".
2. words[1] = "backdoor" and words[6] = "door".
3. words[2] = "gammon" and words[3] = "backgammon".

For words = ["cba", "a", "a", "b", "ba", "ca"], the output should be solution(words) = 8.

The relevant pairs are:
1. words[0] = "cba" and words[1] = "a".
2. words[0] = "cba" and words[2] = "a".
3. words[0] = "cba" and words[4] = "ba".
4. words[1] = "a" and words[2] = "a".
5. words[1] = "a" and words[4] = "ba".
6. words[1] = "a" and words[5] = "ca".
7. words[2] = "a" and words[4] = "ba".
8. words[2] = "a" and words[5] = "ca".

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.string words

An array of strings containing lowercase English letters.

Guaranteed constraints:
1 ≤ words.length ≤ 105,
1 ≤ words[i].length ≤ 10.

[output] integer64

The number of pairs where one string is a suffix of the other string.
"""