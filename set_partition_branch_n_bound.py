import pickle
import os
import time
import sys
from memory_profiler import memory_usage
import psutil
sys.setrecursionlimit(131072)
def partition_values_from_index(values, start_index, total_value, unassigned_value, test_assignment, 
                                test_value, best_assignment, best_err):
    if start_index >= len(values):
        # We're done. See if this assignment is better than what we have so far.
        test_err = abs(2 * test_value - total_value)
        if test_err < best_err[0]:
            # This is an improvement. Save it.
            best_err[0] = test_err
            best_assignment[:] = test_assignment[:]

            # print(best_err[0])
    else:
        # See if there's any way we can assign the remaining items to improve the solution.
        test_err = abs(2 * test_value - total_value)
        if test_err - unassigned_value < best_err[0]:
            # There's a chance we can make an improvement.
            # We will now assign the next item.
            unassigned_value -= values[start_index]

            # Try adding values[start_index] to set 1.
            test_assignment[start_index] = True
            partition_values_from_index(values, start_index + 1, total_value, unassigned_value, 
                                        test_assignment, test_value + values[start_index], best_assignment, best_err)

            # Try adding values[start_index] to set 2.
            test_assignment[start_index] = False
            partition_values_from_index(values, start_index + 1, total_value, unassigned_value, 
                                        test_assignment, test_value, best_assignment, best_err)

def run_partition_algorithm(dataset):
    values = dataset
    start_index = 0
    total_value = sum(values)
    unassigned_value = total_value
    test_assignment = [False] * len(values)
    test_value = 0
    best_assignment = [False] * len(values)
    best_err = [float('inf')]
    partition_values_from_index(values, start_index, total_value, unassigned_value, test_assignment, test_value, best_assignment, best_err)
    
    print("Dataset:", values)
    print("Best Assignment:", best_assignment)
    print("Best Error:", best_err)
    
    if best_err[0] == 0:
        print("Can be divided into two subsets of equal sum")
    else:
        print("Can not be divided into two subsets of equal sum")
    print()

if __name__ == "__main__":
    dataset_folder = "dataset"

    # List all files in the dataset folder
    dataset_files = [file for file in os.listdir(dataset_folder) if file.endswith(".pkl")]
    dataset_files.sort(reverse=True)
    # Load and run the partition algorithm on each dataset
    for file in dataset_files:
        file_path = os.path.join(dataset_folder, file)
        with open(file_path, 'rb') as f:
            dataset = pickle.load(f)
            start_time = time.perf_counter()
            process = psutil.Process(os.getpid())
            start_memory = process.memory_info().rss
            run_partition_algorithm(dataset)
            end_memory = process.memory_info().rss
            mem_usage = (end_memory - start_memory) / (1024 ** 2)
            end_time = time.perf_counter()
            execution_time = (end_time - start_time)
            print(f"Penggunaan Memori Selama Eksekusi: {(mem_usage)} MiB")
            print(f"Execution time for {f.name}: {execution_time} seconds\n")
