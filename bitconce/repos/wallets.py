from . import Bitconce
from .models import wallet


class WalletsRepo(Bitconce):
    def get_wallets(self, amount: int = 1000, page_number: int = 1) -> list[wallet.Wallet]:
        url_main = "getMyWallets/"
        url_add = 'getExtendedInfoWallets/'
        method = 'GET'
        params = {
            'amount': amount,
            'page_number': page_number
        }

        wallets = self.request(url=url_main, method=method, params=params)
        id_list = ",".join([str(w['id']) for w in wallets])
        params = {
            'id_list': id_list
        }
        adds = self.request(url=url_add, method=method, params=params)
        for idx, add in enumerate(adds):
            for key, value in add.items():
                wallets[idx][key] = value

        return [wallet.Wallet(source) for source in wallets]

    def toggle_enable(self, wallet_id: str, enable: bool) -> bool:
        url = 'toggleEnableWallet/'
        method = 'GET'
        params = {
            'wallet_id': wallet_id,
        }

        response = self.request(url=url, method=method, params=params)
        if response['wallets_status'] != enable:
            return True
        else:
            return False

    def reset_limit(self, number: str) -> bool:
        url = 'refreshWalletLimit/'
        method = 'POST'
        payload = {
            'wallet_number': number
        }
        response = self.request(url=url, method=method, payload=payload)
        if response['status'] == 'success':
            return True
        else:
            return False

    def edit_wallet(self, w: wallet.Wallet, action: str) -> bool:
        url = 'editAutonumber/'
        method = 'POST'
        allowed_actions = 'add', 'edit', 'delete'
        if action not in allowed_actions:
            raise Exception(f"action {action} not in {allowed_actions}")

        payload = {
            'action': action,
            'owner_name': w.owner_name,  # Павел Олегович О.
            'bank_account': w.bank_account,
            'sbp_number': w.sbp_number,
            'wallet': w.number,
            'limit': w.limit,
            'auto_number_off': w.autonumber_off,
            'notify_off': w.notify_off,
            'description': w.description,
        }

        response = self.request(url=url, method=method, payload=payload)
        if response['status'] == 'success':
            return True
        else:
            return False
