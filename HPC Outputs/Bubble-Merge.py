import time
from concurrent.futures import ThreadPoolExecutor


# ---------------- BUBBLE SORT ----------------

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


# ---------------- MERGE SORT ----------------

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


# ---------------- MAIN PROGRAM ----------------

n = int(input("Enter size of array: "))

arr = []

print("Enter elements:")

for i in range(n):

    arr.append(int(input()))


# Copy arrays
bubble_seq_arr = arr.copy()
bubble_par_arr = arr.copy()

merge_seq_arr = arr.copy()
merge_par_arr = arr.copy()


# -------- Sequential Bubble Sort --------

start_time = time.time()

sequential_bubble_sort(bubble_seq_arr)

end_time = time.time()

bubble_seq_time = (end_time - start_time) * 1000


# -------- Parallel Bubble Sort --------

start_time = time.time()

parallel_bubble_sort(bubble_par_arr)

end_time = time.time()

bubble_par_time = (end_time - start_time) * 1000


# -------- Sequential Merge Sort --------

start_time = time.time()

sequential_merge_sort(merge_seq_arr, 0, n - 1)

end_time = time.time()

merge_seq_time = (end_time - start_time) * 1000


# -------- Parallel Merge Sort --------

start_time = time.time()

parallel_merge_sort(merge_par_arr, 0, n - 1)

end_time = time.time()

merge_par_time = (end_time - start_time) * 1000


# ---------------- OUTPUT ----------------

print("\nSorted Array using Sequential Bubble Sort:")

for num in bubble_seq_arr:
    print(num, end=" ")

print("\n\nSequential Bubble Sort Time:", round(bubble_seq_time, 2), "ms")


print("\nSorted Array using Parallel Bubble Sort:")

for num in bubble_par_arr:
    print(num, end=" ")

print("\n\nParallel Bubble Sort Time:", round(bubble_par_time, 2), "ms")


print("\nSorted Array using Sequential Merge Sort:")

for num in merge_seq_arr:
    print(num, end=" ")

print("\n\nSequential Merge Sort Time:", round(merge_seq_time, 2), "ms")


print("\nSorted Array using Parallel Merge Sort:")

for num in merge_par_arr:
    print(num, end=" ")

print("\n\nParallel Merge Sort Time:", round(merge_par_time, 2), "ms")