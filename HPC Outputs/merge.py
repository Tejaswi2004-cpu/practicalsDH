import time
from concurrent.futures import ThreadPoolExecutor


# Merge Function
def merge(arr, left, mid, right):

    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    # Merge two arrays
    while i < len(L) and j < len(R):

        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

        k += 1

    # Remaining elements
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


# Sequential Merge Sort
def sequential_merge_sort(arr, left, right):

    if left < right:

        mid = (left + right) // 2

        sequential_merge_sort(arr, left, mid)

        sequential_merge_sort(arr, mid + 1, right)

        merge(arr, left, mid, right)


# Parallel Merge Sort
def parallel_merge_sort(arr, left, right):

    if left < right:

        mid = (left + right) // 2

        # Parallel execution
        with ThreadPoolExecutor() as executor:

            executor.submit(parallel_merge_sort, arr, left, mid)

            executor.submit(parallel_merge_sort, arr, mid + 1, right)

        merge(arr, left, mid, right)


# Main Program

n = int(input("Enter size of array: "))

arr = []

print("Enter elements:")

for i in range(n):

    arr.append(int(input()))


# Copy arrays
seq_arr = arr.copy()

par_arr = arr.copy()


# Sequential Merge Sort
start_time = time.time()

sequential_merge_sort(seq_arr, 0, n - 1)

end_time = time.time()

seq_time = (end_time - start_time) * 1000


# Parallel Merge Sort
start_time = time.time()

parallel_merge_sort(par_arr, 0, n - 1)

end_time = time.time()

par_time = (end_time - start_time) * 1000


# Output

print("\nSorted Array using Sequential Merge Sort:")

for num in seq_arr:
    print(num, end=" ")


print("\n\nSequential Merge Sort Time:", round(seq_time, 2), "ms")


print("\nSorted Array using Parallel Merge Sort:")

for num in par_arr:
    print(num, end=" ")


print("\n\nParallel Merge Sort Time:", round(par_time, 2), "ms")