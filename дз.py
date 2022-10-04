import re
class Data:
    def __init__(self, full_name, email, file_name, color):
        self.__full_name = full_name
        self.__email = email
        self.__file_name = file_name
        self.__color = color

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def full_name(self, value):
        self.__file_name = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value


with open('MOCK_DATA.txt', 'r', encoding='UTF-8') as file:


    list = []
    readline = file.readline()

    while readline:

        full_name = re.findall(r"(?:^[A-Z][a-z-]+\s[A-Za-z-'. ]+)", readline)
        full_name = ''.join(full_name)


        email = re.findall(r"(?:[A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(?:\.[A-Z|a-z]{2,})", readline)
        email = ''.join(email)

        file_name = re.findall(r"[A-Z](?:[\w\.]+\.[a-z0-9]+)", readline)
        file_name = ''.join(file_name)

        color = re.findall(r"\#......", readline)
        color = ''.join(color)

        data1 = Data(full_name, email, file_name, color)

        list.append(data1)

        readline = file.readline()

file.close()

for i in list:

    with open("fullname.txt", 'a') as fullname:
        fullname.write(i.full_name + '\n')

    with open('email.txt', 'a') as emal:
        emal.write(i.email + '\n')

    with open("filename.txt", 'a') as filename:
        filename.write(i.file_name + '\n')

    with open('color.txt', 'a') as colour:
        colour.write(i.color + '\n')















