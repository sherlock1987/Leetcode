import random
import math
import string

full_tiny = {}
tiny_full = {}

letters = string.ascii_letters + string.digits
print(random.randint(0,6200)%62)
class Codec:
    def encode(self,longurl):
        ans = ''
        one = ''
        for i in range(0,6):
            one = letters[random.randint(0,6200)%62]
            ans = ans + one
        shorturl = "http://tinyurl.com/" + ans
        if longurl in full_tiny:
            pass
        else:
            full_tiny[longurl]  = shorturl
            tiny_full[shorturl] =  longurl
        return(full_tiny[longurl])

    def decode(self,shorturl):
        if shorturl in tiny_full:
            return tiny_full[shorturl]
        else:
            print('no such short url existed')
            pass
url = 'https://leetcode.com/problems/design-tinyurl'
codec = Codec()
short_url = codec.encode(url)
print(codec.decode(short_url))