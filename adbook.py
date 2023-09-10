from datetime import datetime
from collections import UserDict
import pickle
import re


class PhoneException(Exception):
    pass


class EmailException(Exception):
    pass


class BDException(Exception):
    pass


class Field:
    def __init__(self, value) -> None:
        self.__private_value = None
        self.value = value

    @property
    def value(self):
        return self.__private_value

    @value.setter
    def value(self, value):
        self.__private_value = value


class Name(Field):
    pass


class Address(Field):
    pass


class Phone(Field):
    def __init__(self, value) -> None:
        super().__init__(value)

    @Field.value.setter
    def value(self, value: str):
        value = value.strip()
        # перевірка довжини номера та чи всі введені значення є  цифрами
        right_len = len(value) == 10 or len(value) == 12
        if value.isdigit() and right_len:
            Field.value.fset(self, value)
        else:
            raise PhoneException


class Email(Field):
    def __init__(self, value) -> None:
        super().__init__(value)

    @Field.value.setter
    def value(self, value: str):
        result = re.findall(r"[a-zA-z]{1}[\w\.]+@[a-zA-z]+\.[a-zA-z]{2,}", value)
        if result:
            Field.value.fset(self, value)
        else:
            raise EmailException


class Birthday(Field):
    def __init__(self, value) -> None:
        super().__init__(value)

    @Field.value.setter
    def value(self, value: str):
        value.strip()
        # перевірка чи вік є в діавзоні 0 - 150 р
        delta = datetime.now() - datetime.strptime(value, "%d.%m.%Y")
        if (delta.days < 0) or (delta.days > 53000):
            raise BDException
        else:
            Field.value.fset(self, value)


class Record:
    def __init__(
        self,
        name: Name,
        addres: Address = None,
        phone: Phone = None,
        email: Email = None,
        birthday: Birthday = None,
    ):
        self.name = name
        self.addres = addres
        self.phones = list()
        if phone:
            self.phones.append(phone.value)

        self.email = email
        self.birthday = birthday

    def add_email(self, email: Email):
        self.email = email

    def add_bd(self, birthday: Birthday):
        self.birthday = birthday

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def change_phone(self, old_phone, new_phone):
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def get_next_birthday(self, n: str):
        if self.birthday.value:
            birthday_date = datetime.strptime(self.birthday.value, "%d.%m.%Y")
            current_date = datetime.now()
            birthday_date = birthday_date.replace(year=current_date.year)
            delta_days = birthday_date - current_date

            if delta_days.days == (n - 1):
                return f"Через {n} днів день народження в {self.name.value}"
            else:
                return f"Через {n} днів ніхто не святкує день народження"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
        return self.data

    def save_ab(self):
        with open("addressbook.bin", "wb") as file:
            pickle.dump(self.data, file)

    def open_ab(self):
        with open("addressbook.bin", "rb") as file:
            unpacked = pickle.load(file)
            return unpacked

    def find_user(self, search_str: str):
        result = []
        for k, v in self.data.items():
            if search_str in k or search_str in v.phones[0].value:
                result.append((k, v.phones[0].value))
        return result


# функція для обробки винятків
def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            print("Будь ласка, введіть всю необхідну інформацію!")
        except KeyError:
            print("Даний контакт відсутній у книзі контактів!")
        except PhoneException:
            print("Не правильний формат номеру телефона.")
        except EmailException:
            print("Не правильний формат електронної пошти.")
        except BDException:
            print(
                "Дата народження вказано не правильно, виходить ха межі діапазону 0-150"
            )
        except ValueError:
            print("Не правильний формат дати народження. Повинен бути дд.мм.рррр")

    return inner


AB = AddressBook()


@input_error
def add_handler(user_info: str):
    name = user_info[0].lstrip()
    rec = Record(Name(name))
    AB.add_record(rec)
    return f"Користувач{user_info[0]} доданий"


def show_handler(*args):  # потрібно доробити
    return AB


@input_error
def add_number(user_input: str):
    name = user_input[0]
    name = name.lstrip()
    phone = user_input[1]
    rec = AB[name]
    rec.add_phone(Phone(phone))
    return f"Номер {phone} додано до контакту {name}"


@input_error
def add_email(user_input: str):
    name = user_input[0]
    name = name.lstrip()
    email = user_input[1]
    rec = AB[name]
    rec.add_email(Email(email))
    return f"Електронна пошта {email} додано до контакту {name}"


@input_error
def add_birthday(user_input: str):
    name = user_input[0]
    name = name.lstrip()
    bd = user_input[1]
    bd = bd.lstrip()
    rec = AB[name]
    rec.add_bd(Birthday(bd))
    return f"Дата народження {bd} додано до контакту {name}"


COMMANDS = {
    add_handler: "add contact",
    show_handler: "show all",
    add_number: "add phone",
    add_email: "add email",
    add_birthday: "add birthday",
}


def command_parser(user_input: str):
    user_info = user_input.split(",")
    command = user_info[0]

    for key, value in COMMANDS.items():
        if command.lower() == value:
            return key(user_info[1:])
    return (
        "Не відома команда. Спробуйте ще раз! Команду та основні блоки розділіть комами"
    )


def main():
    while True:
        user_input = input("Введіть команду та необхідну інформацію>>> ")
        if user_input.lower() in ["good bye", "exit", "close"]:
            print("Good bye!")
            break
        result = command_parser(user_input)

        print(result)


if __name__ == "__main__":
    main()
