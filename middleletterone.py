
x = 'abc'
y = 'aaaa'

def mid(x):
    if len(x) % 2 == 0:
        return ''
    else: 
        return x[int(len(x)/2)]
print(mid(x))
print(mid(y))

'''
Write a function named mid that takes a string as its parameter. 
Your function should extract and return the middle letter. If
there is no middle letter, your function should return the empty
string.
For example, mid('abc') should 'b' and mid('aaaa') should return "".
'''