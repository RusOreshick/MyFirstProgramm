#контейнер задач
list_task = []

#переменная для ввода команд и задач
command = None

#стартовая надпись
print("Список комманд:\n "
"/all - все задачи\n "
"/del_last - удаляет последнюю задачу\n "
"/help - список команд\n "
"/clear - удаляет все задачи\n")

#функция отвечающая за команды
def commands():
    command = input("Введите задачу или /help чтобы увидеть все команды: ")

    if command == '/help':
        print("Список комманд:\n "
"/all - все задачи\n "
"/del_last - удаляет последнюю задачу\n "
"/help - список команд\n "
"/clear - удаляет все задачи\n")
        command
    elif command == '/del_last':
        list_task.pop()
        print("Задача удалена.\n")
        command
    elif command == '/all':
        print("Ваши задачи:")
        for i, task in enumerate(list_task, 1):
            print(f"{i} {task}\n")
        command
    elif command == '/clear':
        list_task.clear()
        print("Список отчищен\n")
        command
    else:
        list_task.append(command)
        print("Задача создана.\n")

while True:
    commands()

    command = input("Хотите посмотреть созданные задачи (Да/Нет): ")

    if command == 'Да':
        print("Ваши задачи:")
        for i, task in enumerate(list_task, 1):
            print(f"{i} + {task}\n")
    elif command == 'Нет':
        commands()
    else:
        print("Неверная команда!\n")