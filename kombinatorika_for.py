# 1st version
print ("\tSos \tBul \tKet \tGor \tLuk")
count = 1
for dog in [0, 1]:
  for bun in [0, 1]:
    for ketchup in [0, 1]:
      for mustard in [0, 1]:
        for onion in [0, 1]:
          print ("№", count, "\t", end = " ")
          print (dog, "\t", bun, "\t", ketchup, "\t", mustard, "\t", onion)
          count = count + 1
'''
		Sos Bul	Ket	Gor	Luk
№ 1 	 0 	 0 	 0 	 0 	 0
№ 2 	 0 	 0 	 0 	 0 	 1
№ 3 	 0 	 0 	 0 	 1 	 0
№ 4 	 0 	 0 	 0 	 1 	 1
№ 5 	 0 	 0 	 1 	 0 	 0
№ 6 	 0 	 0 	 1 	 0 	 1
№ 7 	 0 	 0 	 1 	 1 	 0
№ 8 	 0 	 0 	 1 	 1 	 1
№ 9 	 0 	 1 	 0 	 0 	 0...
'''

# 2nd version
dog_cal = 140
bun_cal = 120
mus_cal = 20
ket_cal = 80
onion_cal = 40
print ("\tSos \tBul \tKet \tGor \tLuk \tCal")
count = 1
for dog in [0, 1]:
  for bun in [0, 1]:
    for ketchup in [0, 1]:
      for mustard in [0, 1]:
        for onion in [0, 1]:
          total_cal = (bun*bun_cal)+(dog*dog_cal)+(ketchup*ket_cal)+(mustard*mus_cal)+(onion*onion_cal)
          print (count, "\t", end = " ")
          print (dog, "\t", bun, "\t", ketchup, "\t", mustard, "\t", onion, '\t', total_cal)
          count = count + 1

'''
	Sos Bul	Ket	Gor	Luk	Cal
1 	 0 	 0 	 0 	 0 	 0 	 0
2 	 0 	 0 	 0 	 0 	 1 	 40
3 	 0 	 0 	 0 	 1 	 0 	 20
4 	 0 	 0 	 0 	 1 	 1 	 60
5 	 0 	 0 	 1 	 0 	 0 	 80
6 	 0 	 0 	 1 	 0 	 1 	 120
7 	 0 	 0 	 1 	 1 	 0 	 100
8 	 0 	 0 	 1 	 1 	 1 	 140
9 	 0 	 1 	 0 	 0 	 0 	 120...
'''


#3rd version
print ("\tSos \tBul \tKet \tGor \tLuk \tShifr")
count = 1
for dog in [0, 1]:
  for bun in [0, 1]:
    for ketchup in [0, 1]:
      for mustard in [0, 1]:
        for onion in [0, 1]:
          shifr = str(dog)+str(bun)+str(ketchup)+str(mustard)+str(onion)
          print (count, "\t", end = " ")
          print (dog, "\t", bun, "\t", ketchup, "\t", mustard, "\t", onion, '\t', shifr)
          count = count + 1

'''
	Sos Bul	Ket Gor	Luk  Shifr
1 	 0 	 0 	 0 	 0 	 0 	 00000
2 	 0 	 0 	 0 	 0 	 1 	 00001
3 	 0 	 0 	 0 	 1 	 0 	 00010
4 	 0 	 0 	 0 	 1 	 1 	 00011
5 	 0 	 0 	 1 	 0 	 0 	 00100
6 	 0 	 0 	 1 	 0 	 1 	 00101
7 	 0 	 0 	 1 	 1 	 0 	 00110
8 	 0 	 0 	 1 	 1 	 1 	 00111
9 	 0 	 1 	 0 	 0 	 0 	 01000
10 	 0 	 1 	 0 	 0 	 1 	 01001...
'''