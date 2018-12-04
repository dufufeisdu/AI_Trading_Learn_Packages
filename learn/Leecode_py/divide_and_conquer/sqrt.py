def sqrt_dc(num, ls=[i * i for i in range(10)]):
    scale = 1
    while num > 100:
        scale *= 10
        num /= 100
    while num < 1:
        scale /= 10
        num *= 100
    sqrt_int_digit = 0
    for ele in ls:
        if num > ele:
            sqrt_int_digit = ele
        else:
            break
    while num - sqrt_int_digit**2 > 1e-15:
