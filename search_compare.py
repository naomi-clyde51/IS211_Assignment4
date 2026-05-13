import random
import time

def sequential_search(a_list, item):
    start = time.time()
    found = False
    pos = 0
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found, time.time() - start

def ordered_sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1
    return found, time.time() - start

def binary_search_iterative(a_list, item):
    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found, time.time() - start

def binary_search_recursive(a_list, item):
    def _recursive_helper(inner_list, inner_item):
        if len(inner_list) == 0:
            return False
        else:
            midpoint = len(inner_list) // 2
            if inner_list[midpoint] == inner_item:
                return True
            else:
                if inner_item < inner_list[midpoint]:
                    return _recursive_helper(inner_list[:midpoint], inner_item)
                else:
                    return _recursive_helper(inner_list[midpoint + 1:], inner_item)

    start = time.time()
    result = _recursive_helper(a_list, item)
    return result, time.time() - start

def main():
    sizes = [500, 1000, 10000]
    num_lists = 100
    target = 99999999
    
    for size in sizes:
        results = {
        "Sequential Search": 0,
        "Ordered Sequential": 0,
        "Binary Search (Iterative)": 0,
        "Binary Search (Recursive)": 0
        }

        for _ in range(100):
            arrlist = [random.randint(1, 1000000) for _ in range(size)]
            arrlist.sort()  # Make it ordered
            
            _, t1 = sequential_search(arrlist, target)
            _, t2 = ordered_sequential_search(arrlist, target)
            _, t3 = binary_search_iterative(arrlist, target)
            _, t4 = binary_search_recursive(arrlist, target)

            results["Sequential Search"] += t1
            results["Ordered Sequential"] += t2
            results["Binary Search (Iterative)"] += t3
            results["Binary Search (Recursive)"] += t4        

    print(f"Results for list size {size}:")
    for search_name, total_time in results.items():
        time_taken = total_time / num_lists
        print(f"{search_name} took {time_taken:10.7f} seconds to run, on average")
    print()

if __name__ == "__main__":
    main()
