from src.users.model.user import User


class Wallet:
    currencies = ('USDT', 'BTC')

    def __init__(self, user: User, currency: str):
        if currency not in self.currencies:
            raise Exception(f"{currency} not in {self.currencies}")

        self.user = user
        self.currency = currency
        self.balance = 0.0
        self.id: int | None = None
