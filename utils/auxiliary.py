class States:
    class Users:
        START_PRESSED = "START_PRESSED"
        ADDING_NEW_NOTE = "ADDING_NEW_NOTE"
        SEARCHING_CONTACT = "SEARCHING_CONTACT"
        DELETING_CONTACT = "DELETING_CONTACT"
        CHANGING_CONTACT = "CHANGING_CONTACT"
        ADDING_NEW_ROLE = "ADDING_NEW_ROLE"

        class Person:
            NAME_ENTERING = "NAME"
            SURNAME_ENTERING = "SURNAME"
            MIDDLE_NAME_ENTERING = "MIDDLE_NAME"

        class Phone:
            HOME_PHONE = "HOME_PHONE"
            WORK_PHONE = "WORK_PHONE"
            SELF_PHONE = "SELF_PHONE"

        class Address:
            INDEX = "INDEX"
            AREA = "AREA"
            SETTLEMENT = "SETTLEMENT"
            STREET = "STREET"
            HOUSE = "HOUSE"
            CORPUS = "CORPUS"
            FLAT = "FLAT"

        new_contact_states = ["INDEX", "AREA", "SETTLEMENT", "STREET", "HOUSE", "CORPUS", "FLAT", "NAME",
                              "SURNAME", "MIDDLE_NAME", "HOME_PHONE", "WORK_PHONE", "SELF_PHONE",
                              "ADDING_NEW_NOTE"]

        phone_states = ["HOME_PHONE", "WORK_PHONE", "SELF_PHONE"]

        name_states = ["NAME", "SURNAME", "MIDDLE_NAME"]

        address_states = ["INDEX", "AREA", "SETTLEMENT", "STREET", "HOUSE", "CORPUS", "FLAT"]

        numbers_in_address = ["INDEX", "HOUSE", "CORPUS", "FLAT"]

        NOTE = "NOTE"


class Types:
    class Phone:
        HOME = "home_phone"
        WORK = "work_phone"
        SELF = "self_phone"


class Commands:
    ADD_NEW_NOTE = "new_note"
