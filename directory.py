import pickle
from tabulate import tabulate


# файл с данными
def store(arg):
    f = open('directory.data', 'wb')
    f.write(pickle.dumps(arg))
    f.close()


# экспорт данных из файла
# если файл несуществует, возвращается пустое значение словаря
def extract():
    try:
        f = open('directory.data', 'rb')
        result = pickle.load(f)
        f.close()
        return result
    except:
        return {}


class Directory:
    """
    Directory (Справочник)

    Программа хранит данные контактов в словаре.
    Аргументы принимаются от пользователя из командной строки.
    """

    # инициализация словаря
    directory = extract()

    # инициализация аргументов
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    # добавление контакта в словарь
    def addContact(self):
        Directory.directory[self.name] = self.contact
        print("Контакт {0} был добавлен. \n"
              "Обновлённый список:\n"
              "{1}".format(self.name, tabulate(Directory.directory.items(), headers=["ИМЯ", "НОМЕР"], tablefmt="grid")))

    # удаление контакта из словаря
    def delContact(self):
        try:
            del Directory.directory[self.name]
            print("Контакт {0} был удалён. \n"
                  "Обновлённый список:\n"
                  "{1}".format(self.name,
                               tabulate(Directory.directory.items(), headers=["ИМЯ", "НОМЕР"], tablefmt="grid")))
        except KeyError:
            print("Контакт уже отсутсвует.")

    # поиск контакта в словаре
    def findContact(self):
        self.contact = Directory.directory[self.name]
        if self.name in Directory.directory:
            print("Контакт {0} найден, его номер: {1}".format(self.name, self.contact))
        else:
            print("Контакт {0} отсутствует.".format(self.name))

    # редактирование контакта в словаре
    def editContact(self):
        try:
            print("!!! Если вы не хотите менять параметр, оставьте поле пустым")
            newname = input("Введите новое имя: ")
            newcontact = input("Введите новый номер: ")

            if newname != '' and newcontact != '':
                Directory.directory[newname] = Directory.directory.pop(self.name)
                Directory.directory[newname] = newcontact
                print("Имя и номер контакта успешно изменены.\n"
                      "Обновлённый список:\n"
                      "{0}".format(tabulate(Directory.directory.items(), headers=["ИМЯ", "НОМЕР"], tablefmt="grid")))

            elif newname != '' and newcontact == '':
                Directory.directory[newname] = Directory.directory.pop(self.name)
                print("Имя контакта успешно изменено.\n"
                      "Обновлённый список:\n"
                      "{0}".format(tabulate(Directory.directory.items(), headers=["ИМЯ", "НОМЕР"], tablefmt="grid")))

            elif newname == '' and newcontact != '':
                Directory.directory[self.name] = newcontact
                print("Номер контакта успешно изменён.\n"
                      "Обновлённый список:\n"
                      "{0}".format(tabulate(Directory.directory.items(), headers=["ИМЯ", "НОМЕР"], tablefmt="grid")))

            else:
                return print("Вы не ввели новые значения. Контакт не был изменён")
        except KeyError:
            print("Упс. Что-то пошло не так. Возможно, данный контакт отсутсвует.")


# меню выбора действия
def action():
    choose = int(input("Какое действие Вы хотите выполнить?\n"
                       "\t1 - показать все контакты\n"
                       "\t2 - добавить новый контакт\n"
                       "\t3 - изменить существующий контакт\n"
                       "\t4 - проверить наличие контакта\n"
                       "\t5 - удалить существующий контакт\n"
                       ""))
    if choose in range(1, 6):
        return choose
    else:
        print("Неверное значение. Попробуйте еще раз: ")
        action()


# выполнение выбранного действия
def start():
    choose = action()
    if choose == 1:
        print(tabulate(Directory.directory.items(), headers=["ИМЯ", "НОМЕР"], tablefmt="grid"))
    elif choose == 2:
        name = input("Введите имя: ")
        contact = input("Введите номер: ")
        person = Directory(name, contact)
        Directory.addContact(self=person)
    elif choose == 3:
        name = input("Введите имя: ")
        person = Directory(name, contact='')
        Directory.editContact(self=person)
    elif choose == 4:
        name = input("Введите имя: ")
        Directory.findContact(Directory(name, ''))
    elif choose == 5:
        name = input("Введите имя: ")
        Directory.delContact(Directory(name, ''))


# запуск программы
if __name__ == "__main__":
    run = True
    while run:
        start()
        ask = input("Для выхода введите \"0\", для продолжения - что-угодно: ")
        if ask == "0":
            print("До свидания!")
            break
        else:
            continue

# сохранение данных в файле
store(Directory.directory)
