import timeit
import matplotlib.pyplot as plt
from functools import lru_cache
from splay_tree import SplayTree

@lru_cache
def fibonacci_lru(n):
    if n < 2:
        return n
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)

def fibonacci_splay(n: int, tree: SplayTree):
    cache_result = tree.find(n)
    if cache_result is not None:
        return cache_result
    if n < 2:
        result = n
    else:
        result = fibonacci_splay(n - 1, tree) + fibonacci_splay(n - 2, tree)
    
    tree.insert(n, result)
    return result

tree = SplayTree()

n_values = list(range(0, 951, 50))
lru_times = []
splay_times = []
number_of_tests = 100

for n in n_values:
    lru_time = timeit.timeit(lambda: fibonacci_lru(n), number=number_of_tests)
    splay_time = timeit.timeit(lambda: fibonacci_splay(n, tree), number=number_of_tests)
    lru_times.append(lru_time)
    splay_times.append(splay_time)

plt.figure(figsize=(10, 5))
plt.plot(n_values, lru_times, label='LRU Cache', marker='o')
plt.plot(n_values, splay_times, label='Splay Tree', marker='x')
plt.xlabel('Число Фібоначчі (n)')
plt.ylabel(f"Середній час виконання {number_of_tests} разів")
plt.title('Порівняння часу виконання LRU Cache і Splay Tree')
plt.legend()
plt.grid()
plt.show()

print("{:>5} {:>18} {:>18}".format("n", "LRU Cache (s)", "Splay Tree (s)"))
print("-" * 45)
for i in range(len(n_values)):
    print("{:>5} {:>18.8f} {:>18.8f}".format(n_values[i], lru_times[i], splay_times[i]))