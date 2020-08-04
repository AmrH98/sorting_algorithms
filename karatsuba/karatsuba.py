def karatsubaMulti(x, y):
    # X and Y n-digit string in base B
    #  m < n
    #   example: x = x1 B^m + x0
    #  x0 and y0 less than B^m
    #  z2 = x1y1
    #  z1 = x1y0 + x0y1
    #  z0 = x0y0
    #  result = z2 B^2m + z1B^m + z0


    # convert to string
    xstr = str(x)
    ystr = str(y)
    base = 10
    # check length
    if len(xstr) == 1 or len(ystr) == 1:
        return (x * y)
    else:
        n = max(len(xstr), len(ystr))
        m = n // 2;
        # split integer at m
        a = x // base**(m) #x1
        b = x % base**(m)  #x0
        c = y // base**(m) #y1
        d = y % base**(m)  #y0

        z2 = karatsubaMulti(a,c)
        z1 = karatsubaMulti((a+b), (c+d))
        z0 = karatsubaMulti(b,d)
        z1 = z1 - z2 - z0


        #result
        return ((z2*(base**(2*m))) + (z1*(base**m)) + z0)


x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

result = karatsubaMulti(x,y)
print(result)
