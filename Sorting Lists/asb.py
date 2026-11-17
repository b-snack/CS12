arr = [2, 3, 4, 5]
n = len(arr)
for j in range(0, n-1):
  for i in range(0, n-1):
    if arr[n] > arr[n+1]:
      arr[n], arr[n+1] = arr[n+1], arr[n]
  for i in range(n-1, 0, -1):
    if arr[n-1] > arr[n]:
      arr[n-1], arr[n] = arr[n], arr[n]