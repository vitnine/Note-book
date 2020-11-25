
class Menu:
    add_new_contact = "Добавить контакт"
    get_contact = "Найти контакт"
    correct_inf = "Изменить контакт"
    delete_contact = "Удалить контакт"
    ask_rights = "Отправить запрос на дополнительные права"


class Choosing:
    class Numbers:
        HOME_PHONE = "Домашний телефон"
        WORK_PHONE = "Рабочий телефон"
        SELF_PHONE = "Личный телефон"

        ALL_PHONES = [HOME_PHONE, WORK_PHONE, SELF_PHONE]

    class Person:
        NAME = "Имя"
        SURNAME = "Фамилия"
        MIDDLE_NAME = "Отчество"

        ALL_NAMES = [NAME, SURNAME, MIDDLE_NAME]

    class Address:
        INDEX = "Индекс"
        AREA = "Область"
        SETTLEMENT = "Населенный пункт"
        STREET = "Улица"
        HOUSE = "Дом"
        CORPUS = "Корпус"
        FLAT = "Квартира"

        ALL_ADDRESSES = [INDEX, AREA, SETTLEMENT, STREET, HOUSE, CORPUS, FLAT]

    ALL_CHOOSES = [Numbers.SELF_PHONE, Numbers.WORK_PHONE, Numbers.HOME_PHONE,
                   Person.SURNAME, Person.NAME, Person.MIDDLE_NAME,
                   Address.INDEX, Address.AREA, Address.SETTLEMENT, Address.STREET,
                   Address.HOUSE, Address.CORPUS, Address.FLAT]
    second_back = "Назад"
    back = "Вернуться"
    confirm = "Завершить"
