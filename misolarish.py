from random import randrange
d = randrange(10,100)
a_missiv = []
b = []
for i in range(d):
    h_toq = randrange(100,200)
    a_missiv.append(h_toq)


for i in range(len(a_missiv)):
    if i % 3 == 0:
        b.append(i)
    else:
        print("ishlamdi😫")
print(b)
print(type(b))