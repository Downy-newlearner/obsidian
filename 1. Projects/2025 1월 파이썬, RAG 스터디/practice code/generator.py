import time

def fibon(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result


#start = time.time()
#for x in fibon(100000):
#    pass

#end = time.time()
#print('total time: ', end - start)

def fibon_generator(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

start = time.time()
for x in fibon_generator(100000):
    pass

end = time.time()

print('total time: ', end - start)
