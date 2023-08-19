import re


class Requisite:
    directions = ("CARD", "SBP", "QIWI")

    def __init__(self,
                 direction: str,
                 number: str,
                 owner: str,
                 account: str,
                 platform_token: str,
                 user_telegram: str,
                 wallet_currency: str):
        if direction not in self.directions:
            raise Exception(f"{direction} not in {self.directions}")

        number = re.sub(r'[\D]+', '', number)

        valid, message = self.validate_number(number, direction)
        if not valid:
            raise Exception(message)
        self.direction = direction

        self.number = number

        valid, message = self.validate_owner(owner)
        if not valid:
            raise Exception(message)
        self.owner = owner

        self.account = account
        self.platform_token = platform_token
        self.user_telegram = user_telegram
        self.wallet_currency = wallet_currency
        self.is_active = False
        self.is_hidden = False

        self.description = None
        self.limit = 100_000
        self.auto_number_off = False
        self.notify_off = False

        if direction == 'SBP':
            self.sbp_number = number

    def validate_number(self, number: str, direction: str) -> (bool, str):
        if direction == "CARD":
            if len(number) != 16:
                return False, "Номер карты должен состоять из 16 цифр"
        if direction == "SBP":
            if len(number) != 11:
                return False, "Номер телефона должен состоять из 11 цифр"
        if direction == 'QIWI':
            if len(number) != 11:
                return False, "Номер телефона кошелька должен состоять из 11 цифр"

        return True, None

    def validate_owner(self, owner: str) -> (bool, str | None):
        if not re.match(r'[А-ЯЁ][а-яё]+\s[А-ЯЁ][а-яё]+\s[А-ЯЁ]\.', owner):
            return False, "ФИО должно соответствовать шаблону: Имя Фамилия О."

        return True, None
