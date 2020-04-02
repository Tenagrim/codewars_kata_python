def high_and_low(numbers):
    x = numbers.split()
    h = int(x[0])
    l = int(x[0])
    for n in x:
        if int(n) > h:
            h = int(n)
        elif int(n) < l:
            l = int(n)
    return (str(h)  + " " + str(l))

print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
