def rand_seq(length):
    import random
    seq = ""
    while True:
        if "3" in seq and "7" in seq:
            break
        seq = "".join([str(random.randint(0, 9)) for num in range(length)])
    return seq
rand_seq(26)