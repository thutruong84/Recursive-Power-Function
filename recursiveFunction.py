def power(x,n):
    '''
    Function to raise x to the nth power
    '''
    # change x from string to float
    x = float(x)
    # change x from string to integer
    n = int(n)
    # if n is 0, then result is 1
    if n == 0:
        result = 1
    # if n is even, then result = (recursive function of x^(n/2)) * (recursive function of x^(n/2))
    elif (n % 2) == 0:
        result = power(x,n/2) * power(x,n/2)
    # if n is odd, then result = x * (recursive function of x^(n/2)) * (recursive function of x^(n/2))
    # since the power funcion makes (n/2) an integer, it will be round down
    # for example, if n = 3, n/2 = 1.5, int(n/2) = 1, so result = x * (x^1) * (x^1) = x^3
    else:
        result = x * power(x,n/2) * power(x,n/2)
    return result

# get user's input for x
x = input("Enter x:")

# get user's input for n and check whether it's positive or not
isPositive = -1
while isPositive < 0:
    n = input("Enter n (positive whole number only):")
    isPositive = int(n)

# compute the function and print out result
print(str(power(x,n)))
