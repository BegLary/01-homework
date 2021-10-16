def sqrd_list(sqrd): 
    for i in sqrd:
        print(i**2, end=" ")

a=list(range(10))
sqrd_list(a)
print('---')

b=list(range(100))
sqrd_list(b)
print('---')

c=list()
sqrd_list(c)
print('---')