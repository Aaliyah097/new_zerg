from . import Bitconce
from .models import (
    account,
    rate
)


class AccountsRepo(Bitconce):
    def get_account_info(self) -> account.Account:
        url = "getAccountInfo/"
        method = 'GET'
        return account.Account(self.request(url, method))

    def get_rate(self) -> rate.Rate:
        url = "getMyRate/"
        method = 'GET'
        return rate.Rate(self.request(url, method))

    def toggle_deals(self, enabled: bool) -> bool:
        url = 'toggleSellerDealEnable/'
        method = 'POST'
        payload = {'status': enabled}

        response = self.request(url, method, payload)
        try:
            if response['seller_deal_enable'] != enabled:
                return True
            else:
                return False
        except KeyError:
            return False

    def transfer_balance(self, account_id: int, amount: float):
        url = 'balanceTransfer/'
        method = 'POST'
        payload = {
            'to_id': account_id,
            'amount': amount
        }

        response = self.request(url=url, method=method, payload=payload)
        print(response)
