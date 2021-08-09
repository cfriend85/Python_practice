# loop through up until given number(n) and square all values beneath it
for i in range(n): print(i*i)

def is_leap(year):
    leap = False
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    
    return leap

# loop through starting at one and being inclusive on n and add them to the string and print it
str = ""
for i in range(1, n+1): str += f"{i}"
print (str)