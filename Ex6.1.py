# list comprehensions
lc1=[x*2 for x in range(5)]
print(lc1)
lc2=[w[1] for w in ['hello','world','how','goes','it?']]
print(lc2)
lc3=[word[::-1]*2 for word in ['hello','bye','no']]
print(lc3)
lc4=[x**2 for x in range(1,10) if x%2==0]
print(lc4)
lc5=[c in 'aeiou' for c in 'cu see you']
print(lc5)