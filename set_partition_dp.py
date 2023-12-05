# Dynamic Programming based python
# program to partition problem
 
# Returns true if arr[] can be
# partitioned in two subsets of
# equal sum, otherwise false
 
import pickle
import os
import time
import sys
sys.setrecursionlimit(131072)
from memory_profiler import memory_usage

def findPartition(arr, n):
    sum = 0
    i, j = 0, 0
 
    # calculate sum of all elements
    for i in range(n):
        sum += arr[i]
 
    if sum % 2 != 0:
        return False
 
    part = [[True for i in range(n + 1)]
            for j in range(sum // 2 + 1)]
 
    # initialize top row as true
    for i in range(0, n + 1):
        part[0][i] = True
 
    # initialize leftmost column,
    # except part[0][0], as 0
    for i in range(1, sum // 2 + 1):
        part[i][0] = False
 
    # fill the partition table in
    # bottom up manner
    for i in range(1, sum // 2 + 1):
 
        for j in range(1, n + 1):
            part[i][j] = part[i][j - 1]
 
            if i >= arr[j - 1]:
                part[i][j] = (part[i][j] or
                              part[i - arr[j - 1]][j - 1])
    # print(part)
    return part[sum // 2][n]

def run_partition_algorithm(dataset):
        n = len(dataset)

        if findPartition(dataset, n):
            print("Dataset:", dataset)
            print("Can be divided into two subsets of equal sum")
        else:
            print("Dataset:", dataset)
            print("Can not be divided into two subsets of equal sum")
        print()
 
# Driver Code
if __name__ == "__main__":
    arr = [1,2,3]
    n = len(arr)
    
    # Function call
    if findPartition(arr, n) == True:
        print("Can be divided into two",
            "subsets of equal sum")
    else:
        print("Can not be divided into ",
            "two subsets of equal sum")
    print("-----------------------------------------")
    
    # This code is contributed
    # by mohit kumar 29


    dataset_folder = "dataset"

    # List all files in the dataset folder
    dataset_files = [file for file in os.listdir(dataset_folder) if file.endswith(".pkl")]

    # Load and run the partition algorithm on each dataset
    for file in dataset_files:
        file_path = os.path.join(dataset_folder, file)
        with open(file_path, 'rb') as f:
            dataset = pickle.load(f)
            start_time = time.perf_counter()
            run_partition_algorithm(dataset)
            end_time = time.perf_counter()
            mem_usage = memory_usage((findPartition, (dataset, len(dataset),)), interval=0.1, timeout=200)
            execution_time = (end_time - start_time)
            print(f"Penggunaan Memori Selama Eksekusi: {max(mem_usage)} MiB")
            print(f"Execution time for {f.name}: {execution_time} seconds\n")
