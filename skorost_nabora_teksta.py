import time, datetime, random

messages = [
"Из всех деревьев мы врезались в то, которое смогло дать нам сдачи.",
"Если не прекратить его попытки спасти вам жизнь, он вас убьет.",
"Нашу сущность намного лучше демонстрируют действия, а не возможности.",
"Я маг, а не размахивающий палкой бабуин.",
"Величие порождает зависть, зависть — злобу, злоба — ложь.",
"В мечтах мы попадаем в наш и только наш мир.",
"Я убежден, что истина, как правило, предпочтительнее лжи.",
"Казалось, что рассвет следует за полночью с неприличной поспешностью."
]

print ("Проверка скорости набора. Введите следующую фразу. Я засеку время.")
time.sleep(2)
print ("\nПриготовиться...")
time.sleep(1)
print ("\nСосредоточиться...")
time.sleep(1)
print ("\nНачали:")
message = random.choice(messages)
print ("\n " + message)
start_time = datetime.datetime.now()
typing = input('>')
end_time = datetime.datetime.now()
diff = end_time - start_time
typing_time = diff.seconds + diff.microseconds / float(1000000)
cps = len(message) / typing_time
wpm = cps * 60 / 5.0
print ("\nВы ввели %i символов за %.1f секунд." % (len(message),typing_time))
print ("Это %.2f символов в секунду, или %.1f слов в минуту" %(cps, wpm))
if typing == message:
  print ("Вы не сделали ни одной ошибки.")
else:
  print ("Но вы сделали по крайней мере одну ошибку.")