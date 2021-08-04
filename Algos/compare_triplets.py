def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i in range (0, len(b)):
        if a[i] > b[i]:
            alice += 1
        elif b[i] > a[i]:
            bob += 1
        elif a[i] == b[i]:
            print("Tie!")
    return [alice, bob]