s="abcdefghijklmnopqrstuvwxyz"
#a
s[0:13]
print(s[0:len(s)//2])
#b
print(s[:len(s)//2])
#c
s[len(s)//2]:(len(s)) # type: ignore
#d
print(s[len(s)//2:])
#e
print(s[0:len(s):2])
#f
s[::-1]
#g
print(s[::-3])