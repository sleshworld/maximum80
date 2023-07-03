# написать функцию, которая считает число каждого символа в строчке
# например "aaaabbcddd"
# 4 a
# 2 b
# 1 c
# 3 d
import time

def counter(s): # если у нас N букв сложность O(N^2) or O(N**2)
    for let in s:
        count = 0
        for sub_let in s:
            if let == sub_let:
                count += 1
        #print(let, count)
start = time.time()
for i in range(1_500_000):
    counter("queue")
end = time.time()
print(end - start)

# set() - ???
# set - множество - уникальные элементы, неупорядоченный
def counter(s): # O(N*M) - M число уникальных букв, худший N^2 = N*M когда M=N 
    for let in set(s): # M
        count = 0
        for sub_let in s: # N - число букв в целом
            if let == sub_let:
                count += 1
        #print(let, count)
start = time.time()
for i in range(1_500_000):
    counter("queue")
end = time.time()
print(end - start)

#start = time.time()
#for i in range(1_500_000):
    #counter("quetr")
#end = time.time()
#print(end - start)


def counter(s): # O(N)
    let_counter = {}
    for let in s:
        let_counter[let] = let_counter.get(let, 0) + 1
    #print(let_counter)

counter("queue")

start = time.time()
for i in range(1_500_000):
    counter("queue")
end = time.time()
print(end - start)