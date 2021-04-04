from functools import reduce

list_1 = range(9)
list_2 = ["Hi", "Hello", "Cao", "Ahoj", "Cau", "Hola", "Halo"]

#map function 
print(list(map(len, list_2)))
print(list(map(lambda x: (x, -x), list_1)))
print(list(map(lambda two: two+"hi", list_2)))
print(list(map(lambda square: square**2, list_1)))


#filter funciton 
print(list(filter(lambda odd: odd % 2 != 0, list_1)))
print(list(filter(lambda even: even % 2 == 0, list_1)))


#reduce function

def reduce_sum(a, b):
    return a + b

def product(a,b):
    return a * b

print(reduce(reduce_sum, list_1))

print(reduce(product, range(1,3)))