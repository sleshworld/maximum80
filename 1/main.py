def strcounter(s):
    for sym in s:
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter += 1
        #print(sym, counter)

strcounter('aabbbbccd')
setup= '''
def strcounter(s): #решение за N**2
    for sym in s:
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter += 1
        #print(sym, counter)
'''
from timeit import timeit
print(timeit("strcounter('aabbbbccd')", setup=setup, number=1000000))

from time import time
start = time()
for i in range(1000000):
    strcounter('aabbbbccd')
end = time()
print(end-start)
def strcounter(s): # решение за N * M
    for sym in set(s):
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter += 1
        #print(sym, counter)

strcounter('aabbbbccd')
from time import time
start = time()
for i in range(1000000):
    strcounter('aabbbbccd')
end = time()
print(end-start)
def strcounter(s): # решение за N
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1

    for sym, count in syms_counter.items():
        pass
        #print(sym, count)
strcounter('aabbbbccd')

from time import time
start = time()
for i in range(1000000):
    strcounter('aabbbbccd')
end = time()
print(end-start)