# Solution given by greg hogg
from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = defaultdict(int)
        balloon = 'balloon'

        for c in text:
            if c in balloon:
                counter[c] += 1
        
        if any(c not in counter for c in balloon):
            return 0
        else:
            return min(counter['b'], counter['a'], counter['l']//2, counter['o']//2, counter['n'])
        


'''
# My own solution
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
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
                    return count
            count += 1
'''