import time
import random
import matplotlib.pyplot as plt
import gc
from statistics import median

def insertion_sort(arr):
    result = arr[:]
    
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result

def merge_sort(arr):

    if len(arr) <= 1:
        return list(arr)
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def random_list(n):
    answer = [] 
    for i in range(n):
        answer.append(random.randint(0, 1000000))
    return answer

def disorder_list(n, disorder):
    answer = []
    for i in range(n):
        answer.append(i)
    for i in range(disorder): # disorder swaps n random elements
        a1 = random.randint(0, n-1)
        a2 = random.randint(0, n-1)
        answer[a1], answer[a2] = answer[a2], answer[a1]
    return answer

def run_question_1(min_n, max_n, points, trials):
    step = max((1, (max_n - min_n) // (points - 1)))
    lengths = list(range(min_n, max_n + 1, step))

    insertion_times = []
    merge_times = []
    python_times = []

    gc.disable()
    try:
        for i in lengths:
            ins_time = []
            merge_time = []
            python_time = []

            for trial in range(trials):
                l = random_list(i)
                l_merge = l[:]
                l_ins = l[:]
                l_python = l[:]

                start = time.perf_counter()
                _ = insertion_sort(l_ins)
                end = time.perf_counter()
                ins_time.append(end - start)

                start = time.perf_counter()
                _ = merge_sort(l_merge)
                end = time.perf_counter()
                merge_time.append(end - start)

                start = time.perf_counter()
                _ = sorted(l_python)
                end = time.perf_counter()
                python_time.append(end - start)

            insertion_times.append(median(ins_time))
            merge_times.append(median(merge_time))
            python_times.append(median(python_time))

    finally:
        gc.enable()

    
    plt.plot(lengths, insertion_times, label = "Insertion Sort", color = "red")
    plt.plot(lengths, merge_times, label = "Merge Sort", color = "blue")
    plt.plot(lengths, python_times, label = "Python Sort", color = "green", linestyle = "--")

    plt.xlabel("Elements Sorted")
    plt.ylabel("Time Taken")
    plt.title("Time Taken for Elements Sorted in Different Lists")
    plt.legend()
    plt.show()
    
run_question_1(1, 100, 100, 2500)

