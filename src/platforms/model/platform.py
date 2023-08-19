from abc import ABC, abstractmethod


class Platform(ABC):
    sources = ('bitconce', )

    def __init__(self,
                 source: str,
                 token: str,
                 name: str = None):
        self.source = source if source in self.sources else 'untitled'
        self.token = token
        self.name = name if name else token
        self.balance = 0
        self.currency = None
        self.is_active = False
        self.direction = None

    @abstractmethod
    def initialize(self):
        raise NotImplementedError()

    def toggle_deals(self):
        raise NotImplementedError()
