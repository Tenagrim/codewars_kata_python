# return masked string
def maskify(cc):
    if len(cc) <= 4:
        return(cc)
    str = cc[(len(cc) - 4) : (len(cc))]
    print(cc)
    print(str)
    return ((len(cc)-4) * "#" + str)
