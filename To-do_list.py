#список для незавершенных задач
unfinished_task = []

#список для завершенных задач
completed_task = []

#переменная для ввода команд и задач
command = None

#стартовая надпись
print("Список комманд:\n "
"/all - все не завершные задачи\n "
"/del_last - удаляет последнюю задачу\n "
"/help - список команд\n "
"/clear - удаляет все задачи\n "
"/complete - завершает последнюю задачу\n "
"/compt - показывает все завершные задачи\n")

#функция отвечающая за команды
def commands():
    command = input("Введите задачу или /help чтобы увидеть все команды: ")

    if command == '/help':
        print("Список комманд:\n "
"/all - все задачи\n "
"/del_last - удаляет последнюю задачу\n "
"/help - список команд\n "
"/clear - удаляет все задачи\n "
"/complete - завершает последнюю задачу "
"/compt - показывает все завершные задачи\n")
        command
    elif command == '/del_last':
        unfinished_task.pop()
        print("Задача удалена.\n")
        command
    elif command == '/all':
        print("Ваши задачи:")
        for i, task in enumerate(unfinished_task, 1):
            print(f"{i} {task}\n")
        command
    elif command == '/clear':
        unfinished_task.clear()
        print("Список отчищен\n")
        command
    elif command == '/complete':
        element = unfinished_task.pop()
        completed_task.append(element)
        command
    elif command == '/compt':
        for el, task in enumerate(completed_task, 1):
            print(f"{el} {task}\n")
        command
    else:
        unfinished_task.append(command)
        print("Задача создана.\n")

while True:
    commands()

    command = input("Хотите посмотреть созданные задачи (Да/Нет): ")

    if command == 'Да':
        print("Ваши задачи:")
        for i, task in enumerate(unfinished_task, 1):
            print(f"{i} + {task}\n")
    elif command == 'Нет':
        commands()
    else:
        print("Неверная команда!\n")