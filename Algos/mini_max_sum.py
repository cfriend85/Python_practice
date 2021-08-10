def miniMaxSum(arr):
    arr.sort()
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    print(sum - arr[4], sum - arr[0])