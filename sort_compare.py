import argparse
# other imports go here

import time
import random

def insertion_sort(a_list):
    start = time.time()
    for index in range(1, len(a_list)):
        base_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > base_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = base_value
    return time.time() - start

def shell_sort(a_list):
    start = time.time()
    list_count = len(a_list) // 2
    while list_count > 0:
        for start_pos in range(list_count):
            for i in range(start_pos + list_count, len(a_list), list_count):
                current_value = a_list[i]
                position = i
                while position >= list_count and a_list[position - list_count] > current_value:
                    a_list[position] = a_list[position - list_count]
                    position = position - list_count
                a_list[position] = current_value
        list_count = list_count // 2
    return time.time() - start



def python_sort():
    start = time.time()
    a_list.sort()
    return time.time() - start

def main():
    sizes = [500, 1000, 5000]

    for size in sizes:
        results = {
            "Insertion Sort": 0.0,
            "Shell Sort": 0.0,
            "Python Sort": 0.0
        }

        for _ in range(100):
            arrlist = [random.randint(1, 1000000) for _ in range(size)]

            results["Insertion Sort"] += insertion_sort(arrlist[:])
            results["Shell Sort"] += shell_sort(arrlist[:])
            results["Python Sort"] += python_sort(arrlist[:])

        print(f"Results for list size {size}:")
        for name, time_taken in results.items():
            print(f"{name} took {time_taken / 100:.6f} seconds to run, on average")
        print()

if __name__ == "__main__":
    main()
