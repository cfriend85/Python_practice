def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    for i in range(0, len(arr)):
        if arr[i] > 0:
            pos += 1
        elif arr[i] < 0:
            neg += 1
        else:
            zero += 1
    posRatio = pos / len(arr)
    negRatio = neg / len(arr)
    zeroRatio = zero / len(arr)
    
    print(posRatio)
    print(negRatio)
    print(zeroRatio)