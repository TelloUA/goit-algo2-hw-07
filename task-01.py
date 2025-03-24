import time
import random
from functools import lru_cache

def range_sum_no_cache(array, L, R):
    return sum(array[L:R+1])

def update_no_cache(array, index, value):
    # print(f"Index {index}, value {value}")
    array[index] = value

@lru_cache(maxsize=1000)
def range_sum_with_cache(array, L, R):
    return sum(array[L:R+1])

@lru_cache(maxsize=1000)
def update_with_cache(array, index, value):
    array[index] = value

def create_array():
    list = []

    len = 100_000
    i = 0
    while i < len:
        i += 1
        list.append(random.randint(0, 10_000))

    return list

def create_requests():
    operations = []

    len = 50_000
    i = 0
    while i < len:
        i += 1
        operation = random.choice(['range', 'update'])
        
        if operation == 'range':
            start = random.randint(0, 100_000)
            end = random.randint(start, 100_000)
            operations.append((operation, start, end))
        elif operation == 'update':
            index = random.randint(0, 100_000 - 1)
            value = random.randint(0, 10_000)
            operations.append((operation, index, value))

    return operations

def run_process_no_cache(array, operations):
    start_time = time.time()
    for operation in operations:
        if operation[0] == 'range':
            range_sum_no_cache(array, operation[1], operation[2])
        elif operation[0] == 'update':
            update_no_cache(array, operation[1], operation[2])

    end_time = time.time()
    elapsed_time = end_time - start_time 
    print(f"Час виконання: {elapsed_time:.6f} секунд")

def run_process_with_cache(array, operations):
    start_time = time.time()
    for operation in operations:
        if operation[0] == 'range':
            range_sum_with_cache(array, operation[1], operation[2])
        elif operation[0] == 'update':
            update_with_cache(array, operation[1], operation[2])

    end_time = time.time()
    elapsed_time = end_time - start_time 
    print(f"Час виконання: {elapsed_time:.6f} секунд")


if __name__ == '__main__':
    array = create_array()
    operations = create_requests()

    # Не зрозуміло, як робити задачу. LRU_cache не дозволяє почистити індекси частоково

    # run_process_no_cache(array, operations)
    run_process_with_cache(array, operations)
