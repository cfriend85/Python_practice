def check(n):
    if n % 2 == 0 and n > 20:
        print("Not Weird")
    elif n % 2 != 0:
        print ("Weird")
    elif n in range(2,6):
        if n % 2 == 0:
            print ("Not Weird")
    elif n in range(6,21):
        if n % 2 == 0:
            print ("Weird")


def simpleArraySum(ar):
    sum = 0
    for i in range (0, len(ar)):
        sum += ar[i]
    return sum

print (simpleArraySum([1,2,3,4,5]))



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