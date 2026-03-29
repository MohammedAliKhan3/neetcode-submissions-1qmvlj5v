class Solution:

    def encode(self, strs: List[str]) -> str:

       s = ''
       for x in range(len(strs)):
        s += str(len(strs[x])) + '#' + strs[x]

       return s 
    def decode(self, s: str) -> List[str]:

       decode = []
       i = 0
       while i < len(s):

        # Extracting Lenght 
        j = i
        while s[j]!='#':
            j+=1

        length = int(s[i:j])

        # Extracting word

        word = s[j+1:j+1+length]
        decode.append(word)

        # moving i to next word

        i = j+1+length

       return decode