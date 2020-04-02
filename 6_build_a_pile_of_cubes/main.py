import math

def find_nb(m):
    n = math.sqrt(2 * (math.sqrt(m))) - 1
    print("s_n\t%f" % n)
    while ((n * (n + 1))/2) ** 2 < m:
        n += 1
    s_res = (float((n * (n +1)))/2) * (float((n * (n +1)))/2)
    #s_res = float(((n * (n ))/2) ** 2)
    print("n\t%i " % n)
    print("m\t%i " % m)
    print((n * n+1))
    print((n * (n+1))/2)
    print("s_res\t%f" % s_res)
    if int(s_res) != m:
        return (-1)
    else:
        return int(n)
