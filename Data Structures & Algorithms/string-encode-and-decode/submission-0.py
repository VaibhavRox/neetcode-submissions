class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        #scheme being used is STRING-> len(STRING)#<actual string>
        for i in strs:
            encoded_string+=f"{len(i)}#{i}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs=[]
        i=0
        while i<len(s):
            hash_pos=s.find('#',i)          #start from i , search from there onwards, otherwise might find the same # always
            length=int(s[i:hash_pos])
            word=s[hash_pos+1:hash_pos+length+1]
            decoded_strs.append(word)
            #move pointer to next of last char read
            i=hash_pos+length+1
        return decoded_strs

