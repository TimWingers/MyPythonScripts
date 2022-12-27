def count_sheep(n):
    sheep=""
    for i in range(1, n+1):
        sheep += str(i) + " sheep..."
    return sheep
count_sheep(17)