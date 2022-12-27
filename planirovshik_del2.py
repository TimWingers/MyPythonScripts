#Планировщик дел - 2
help = """
help - напечатать справку по программе.
add - добавить задачу в список
show - напечатать все добавленные задачи.
"""
tasks = []
run = True
while run: #== True
	command = input ("Введите команду: ").lower().lstrip().rstrip()
	if command == "help":
		print (help)
	elif command == "show":
		print (tasks)
	elif command == "add":
		task = input ("Введите название задачи: ")
		tasks.append(task)
		print ("Задача добавлена.")
	else:
		print ("Неизвестная команда.")
		run = False
print("До свидания!")