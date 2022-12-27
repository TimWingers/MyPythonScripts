def find_longest(string):
    spl = string.split(" ")
    counter = []
    for word in spl:
        counter.append(len(word))
    return max(counter)

find_longest("The quick white fox jumped around the massive dog")  #7
find_longest("Take me to tinseltown with you")  #10
find_longest("Sausage chops")  #7
find_longest("Wind your body and wiggle your belly")  #6
find_longest("Lets all go on holiday")  #7