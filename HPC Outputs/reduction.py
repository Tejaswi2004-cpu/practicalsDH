import time
from concurrent.futures import ThreadPoolExecutor


# Function to calculate sum
def calculate_sum(arr):

    return sum(arr)


# Function to calculate minimum
def calculate_min(arr):

    return min(arr)


# Function to calculate maximum
def calculate_max(arr):

    return max(arr)


# Function to calculate average
def calculate_average(arr):

    return sum(arr) / len(arr)


# Main Program

n = int(input("Enter number of elements: "))

arr = []

print(f"Enter {n} elements:")

for i in range(n):

    arr.append(int(input()))


# Start time
start_time = time.time()


# Parallel execution
with ThreadPoolExecutor() as executor:

    future_sum = executor.submit(calculate_sum, arr)

    future_min = executor.submit(calculate_min, arr)

    future_max = executor.submit(calculate_max, arr)

    future_avg = executor.submit(calculate_average, arr)


    total_sum = future_sum.result()

    min_value = future_min.result()

    max_value = future_max.result()

    average = future_avg.result()


# End time
end_time = time.time()

execution_time = (end_time - start_time) * 1000


# Output

print("\nResults:")

print("Sum =", total_sum)

print("Min =", min_value)

print("Max =", max_value)

print("Average =", average)

print("Execution Time:", round(execution_time, 2), "ms")