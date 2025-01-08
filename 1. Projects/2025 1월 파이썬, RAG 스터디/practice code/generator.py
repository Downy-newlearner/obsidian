import time

def fibon(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result


start = time.time()
for x in fibon(1000000):
    pass

end = time.time()
print('total time: ', end - start)
