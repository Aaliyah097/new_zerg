from . import DataMixin


class Rate(DataMixin):
    def __init__(self, source: dict):
        self.rate: float = 0.0
        self.source_rate: float = 0.0
        self.percent: float = 0.0
        self.direction: str = ""
        self.network: str = ""
        self.fiat_currency: str = ""

        super().__init__(source)
