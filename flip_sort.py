def flip(d, a):
    if d == 'L':
        return sorted(a, reverse=True)
    else:
        return sorted(a)
flip('L', [2, 7, 12, 5, 1, 9])