import time
from concurrent.futures import ThreadPoolExecutor

# Sequential Bubble Sort
def sequential_bubble_sort(arr):

    n = len(arr)

    for i in range(n):

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Parallel Bubble Sort
def parallel_bubble_sort(arr):

    n = len(arr)

    for i in range(n):

        start = i % 2

        # Function for compare and swap
        def compare_swap(j):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        # Parallel execution
        with ThreadPoolExecutor() as executor:

            executor.map(compare_swap, range(start, n - 1, 2))


# Main Program

n = int(input("Enter number of elements: "))

arr = []

print("Enter elements:")

for i in range(n):

    arr.append(int(input()))


# Copy arrays for both sorting methods
seq_arr = arr.copy()
par_arr = arr.copy()


# Sequential Bubble Sort
start_time = time.time()

sequential_bubble_sort(seq_arr)

end_time = time.time()

seq_time = (end_time - start_time) * 1000


# Parallel Bubble Sort
start_time = time.time()

parallel_bubble_sort(par_arr)

end_time = time.time()

par_time = (end_time - start_time) * 1000


# Output

print("\nSorted Array using Sequential Bubble Sort:")

for num in seq_arr:
    print(num, end=" ")


print("\n\nSequential Bubble Sort Time:", round(seq_time, 2), "ms")


print("\nSorted Array using Parallel Bubble Sort:")

for num in par_arr:
    print(num, end=" ")


print("\n\nParallel Bubble Sort Time:", round(par_time, 2), "ms")