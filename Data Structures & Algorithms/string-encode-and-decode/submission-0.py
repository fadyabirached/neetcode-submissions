class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for i in range(len(strs)):
            encoded += str(len(strs[i]))+"#"+strs[i]
        
        return encoded      

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j= s.find('#',i)
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            decoded.append(word)
            i = j+1+length
        
        return decoded

