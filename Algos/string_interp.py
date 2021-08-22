txt = "hello, and welcome to my world."


def stringInterp(txt):
    y = txt.split(" ")
    str = ""
    for i in range(len(y)):
        str = str + " " + y[i].capitalize()
    return str
print(stringInterp(txt));