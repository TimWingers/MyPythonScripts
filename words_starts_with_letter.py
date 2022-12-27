import re
def words_by_letter(s, l):
    s = re.sub('[^A-Za-z0-9]+', ' ', s)
    s = s.lower()
    x = s.split()
    z = []
    for el in x:
        if l in el[0]:
            z.append(el)
        else:
            pass
    return z

some_string = "History is always written by the winners. When two cultures clash, the loser is obliterated, and the winner writes the history books - books which glorify their own cause and disparage the conquered foe. As Napoleon once said, 'What is history, but a fable agreed upon?'"
words_by_letter(some_string, 'w')