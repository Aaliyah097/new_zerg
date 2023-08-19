from . import DataMixin
from datetime import datetime


class OrderSell(DataMixin):
    statuses = ('all', 'active', 'paid', 'finished', 'canceled', 'closed', 'checking', 'recalculation')

    def __init__(self, source: dict):
        self.id: int = 0
        self.bet_id = None
        self.fiat_amount: float = 0.0
        self.old_amount: float = 0.0
        self.usdt_amount: float = 0.0
        self.status: str = ""
        self.curse: float = 0.0
        self.bonus_percent: float = 0.0
        self.time_window: int = 0
        self.created_at: datetime = datetime.now()
        self.fromreq: str = ""
        self.awaiting_check: bool = False
        self.wallet_description: str = ""
        self.percent: float = 0.0
        self.requisities: str = ""

        super().__init__(source)

        if self.status not in self.statuses:
            print(f"OrderSell #{self.id} -> {self.status} not in {self.statuses}")
