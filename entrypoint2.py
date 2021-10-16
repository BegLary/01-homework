import timeit

def sqrd_list(sqrd): 
    for i in sqrd:
        print(i**2, end=" ")

a=list(range(10))
sqrd_list(a)

b=list(range(100))
sqrd_list(b)

c=list()
sqrd_list(c)

mycode = '''
def sqrd_list(sqrd): 
    for i in sqrd:
        print(i**2, end=" ")

a=list(range(10))
sqrd_list(a)
'''

print(timeit.timeit(stmt=mycode, number=100))

