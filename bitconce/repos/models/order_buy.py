from . import DataMixin
from datetime import datetime


class OrderBuy(DataMixin):
    statuses = ('Active', 'myActive', 'Finished', 'Canceled', 'Paid')

    def __init__(self, source: dict):
        source['id'] = source['exchange_id']
        del source['exchange_id']

        self.id: int = 0
        self.status: str = ""
        self.direction: str = ""
        self.rub_amount: float = 0.0
        self.usdt_amount: float = 0.0
        self.bonus_fiat: float = 0.0
        self.rate: float = 0.0
        self.canceled_amount: int = 0
        self.created_at: datetime = datetime.now()
        self.expired_at: str = ""
        self.need_to_pay: str = ""
        self.requisites: str = ""

        super().__init__(source)

        if self.status not in self.statuses:
            print(f"OrderBuy #{self.id} -> {self.status} not in {self.statuses}")
