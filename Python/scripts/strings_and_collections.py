#str: immutable sequences of Unicode codepoints
print("It's a good thing")
print('"Yes", he said, "I agree"')

#Zen of Python: Practicality beats purity

line = "first" "second"
print(line)

multiline = """this is a multiline
string"""
print(multiline)

multiline2 = "multine can also be done \n like this"
print(multiline2)

print("this is a \" in a string")
#Escape sequences http://docs.python.org/3/reference/lexical_analysis.htlm#strings

#raw strings
path = r'C:\Users\Oguz\Documents'
print(path)

s = str(432)
print(s)

s = 'asdfas'
print(s[3])

print(type(s[3]))

capital = 'oslo'
print(capital.capitalize())
print(capital)


#bytes: immutable sequences of bytes

bb = b'data bytes'
bbb = b"data"

print(bb.split())



#  list dict

