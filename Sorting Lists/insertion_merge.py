import time
import random
import matplotlib.pyplot as plt

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

def run_question_1(trials):
  merge_time = 0
  insertion_time = 0
  insertion_times = []
  merge_times = []
  for i in range(1, trials):
    l = random_list(i)
    

    start = time.time()
    insertion_arr = insertion_sort(insertion_arr)
    end = time.time()
    insertion_time += (end - start)

    start = time.time()
    merging_arr = merge_sort(merging_arr)
    end = time.time()
    merge_time += (end - start)

    insertion_times.append((i, insertion_time))
    merge_times.append((i, merge_time))




# Example code for trials
trials = 100
merge_time = 0
insertion_time = 0
for i in range(trials):
    l = random_list(1000)
    l1 = l[:]
    l2 = l[:] # try on the same list
    
    start = time.time()
    l1 = merge_sort(l1)
    end = time.time()
    merge_time+=(end-start)
    
    start = time.time()
    l2 = insertion_sort(l2)
    end = time.time()
    insertion_time+=(end-start)
    
print(merge_time)
print(insertion_time)

# Example code for graphing lists
l1 = [0,1,2,3,4,5,6,7]
l2 = [0,1,4,9,16,25,36,49]
l3 = [0,6,12,18,24,30,36,42]
plt.plot(l1, l2, '-')
plt.plot(l1, l3, '-')
plt.xlabel("Elements Sorted")
plt.ylabel("Time Taken")
plt.title("title")
plt.legend(["one","two"])
plt.show()