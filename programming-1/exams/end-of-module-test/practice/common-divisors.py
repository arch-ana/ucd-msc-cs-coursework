def common_divisors(a, b):
    divisors = ()
    for num in range(1, min(a,b)):
        if a%num == 0 and b%num == 0:
            divisors += (num,)

    return divisors

print(common_divisors(12, 24))