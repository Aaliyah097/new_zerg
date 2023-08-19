from . import DataMixin


class Account(DataMixin):
    def __init__(self, source: dict):
        self.base_id = None
        self.balance: float = 0.0
        self.balance_fiat: float = 0.0
        self.percent: float = 0.0
        self.direction: str = ""
        self.fiat_currency: str = ""
        self.crypto_currency: str = ""
        self.notifications: int = 0
        self.escrow: float = 0.0
        self.escrow_fiat: float = 0.0
        self.closed_today: int = 0
        self.recieve_today: int = 0
        self.min_limit: int = 0
        self.max_limit: int = 0
        self.deal_enable: bool = False

        super().__init__(source)
