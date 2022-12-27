def conv2ms(h, m, s):
    return (3600*h + 60*m + s) * 1000

h = 0
m = 1
s = 1
conv2ms(h, m, s)