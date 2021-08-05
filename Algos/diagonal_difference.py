def diagonalDifference(arr):
    x = len(arr)
    main = 0
    sec = 0
    for i in range (0, x, 1):
        main += arr[i][i]
        sec += arr[i][x-i-1]
    
    return abs (main - sec)