from .platform import Platform
from bitconce.repos.accounts import AccountsRepo as BitconceAccountsRepo


class BitconcePlatform(Platform):
    def __init__(self,
                 source: str,
                 token: str,
                 name: str = None):
        super().__init__(source, token, name)
        self.repo = BitconceAccountsRepo(token)
        self.initialize()

    def initialize(self):
        """Подтянуть инфу по аккаунту"""

        account_details = self.repo.get_account_info()
        rate_details = self.repo.get_rate()

        self.balance = account_details.balance
        self.direction = account_details.direction
        self.currency = rate_details.network
        self.is_active = account_details.deal_enable

    def toggle_deals(self):
        """Включить/Выключить сделки"""
        new_state = False if self.is_active else True

        if self.repo.toggle_deals(new_state):
            self.is_active = new_state