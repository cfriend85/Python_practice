def birthdayCakeCandles(candles):
    candles.sort()
    max = 0
    count = 0
    for i in range(len(candles)):
        if candles[i] > max:
            max = candles[i]
            count = 1
        elif candles[i] == max:
            count += 1
    return count 