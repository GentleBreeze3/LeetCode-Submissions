class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels= ("aeiouAEIOU")
        sl = list(s)
        i, j = 0, len(sl)-1

        while i<j:
            if sl[i] not in vowels:
                i+=1
            elif sl[j] not in vowels:
                j-=1
            else:
                sl[i], sl[j] = sl[j], sl[i]
                i+=1
                j-=1
        return ''.join(sl)