def divisible_by(numbers, divisor):
    rez = []
    for x in numbers:
        if x % divisor == 0:
            rez.append(x)
    return rez

numbers = [134, 256, 340, 420, 503, 610]
divisor = 2
divisible_by(numbers, divisor)