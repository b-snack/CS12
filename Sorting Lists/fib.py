def fib_recursive(n):
  if n < 2:
    return n
  else:
    return fib_recursive(n-1) + fib_recursive(n-2)




def fib_list(n):
  if n < 2:
    return n
  else:
    nums = [0, 1]
    for i in range(2, n+1):
      nums.append(nums[i-1]+nums[i-2])

  return nums

print(fib_list(10))

def lucas_list(n):
  if n == 0:
    return 2
  elif n == 1:
    return 1
  else:
    nums = [2, 1]
    for i in range(2, n+1):
      nums.append(nums[i-1]+nums[i-2])

  return nums

print(lucas_list(19))