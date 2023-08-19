from . import DataMixin


class Wallet(DataMixin):
    def __init__(self, source: dict):
        self.id: int = 0
        self.number: str = ""
        self.bank_account: str = ""
        self.enable: bool = False
        self.autonumber_off: bool = False
        self.notify_off: bool = False
        self.description: str = ""
        self.quantity_limit: bool = False
        self.quantity_limit_amount: int = 0
        self.limit: int = 0
        self.banned: bool = False
        self.sum_escrow: float = 0.0
        self.sum_all: float = 0.0
        self.sum_finished: float = 0
        self.order_count_today: int = 0
        self.owner_name: str = ""
        self.sbp_number: str = ""

        super().__init__(source)
