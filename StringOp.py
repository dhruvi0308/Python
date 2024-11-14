c='clark'
u='university'
t='cougars'
print(c[0])
print(u[1:] or t[2:4])
print(u[6:4:-1])
print(c+u)
print(5*c or 3*u[-1] or 4*(u[5]+ c[2]))
answer1=(u[1]+t[1])*5
print(answer1)
answer2=c[0:3]+(t[-1])*2 + t[1] + u[3:5] + c[-2]
print(answer2)
answer3= t[-1] + u[4:6] + u[4] +u[1] + u[7:10]
print(answer3)
answer4 = t[-1]+u[-2]+t[1]+u[1]+u[4]
print(answer4)
answer5=u[2:0:-1]+u[3:1:-1]+u[8]+u[4]
print(answer5)