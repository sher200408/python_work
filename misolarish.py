from random import randrange
d = randrange(1,10)
a_missiv = []
b = []
for i in range(d):
    h_toq = randrange(1,10)
    a_missiv.append(h_toq)

# 1-misol
# for i in range(len(a_missiv)):
#     if i % 3 == 0:
#         b.append(i)
#     else:
#        b_juft.append(i)
# print(b)
# print(b_juft)
# 2-misol
# n = randrange(1,10)
# print(n)
# massiv_bergan_2_darasi =[]
# for i in range(n+1):
#     massiv_bergan_2_darasi.append(2**i)

# print(massiv_bergan_2_darasi)
# 3-misol 
n = 8
A1 = 1
D = 2
temp = A1
sol = [A1]

for i in range(n - 1):
    temp += D
    sol.append(temp)
    
for i in sol:
    print(i, end=' ')
