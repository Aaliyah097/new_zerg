from src.requisites.model.requisite import Requisite
from bitconce.repos.wallets import WalletsRepo
from bitconce.repos.models.wallet import Wallet as BitconceWallet


# TODO нужны супер-логи


class BitconceRequisite(Requisite):
    def __init__(self,
                 direction: str,
                 number: str,
                 owner: str,
                 account: str,
                 platform_token: str,
                 user_telegram: str,
                 wallet_currency: str):
        super().__init__(direction,
                         number,
                         owner,
                         account,
                         platform_token,
                         user_telegram,
                         wallet_currency)
        self.base_id = None
        self.repo = WalletsRepo(self.platform_token)

    def initialize(self) -> None:
        bitconce_wallets = self.repo.get_wallets()

        for wallet in bitconce_wallets:
            if wallet.number == self.number:
                self.base_id = wallet.id
                return

    def to_bitconce_wallet(self) -> BitconceWallet:
        bitconce_wallet = BitconceWallet(source={})

        bitconce_wallet.owner_name = self.owner
        bitconce_wallet.bank_account = self.account
        bitconce_wallet.sbp_number = self.number if self.direction == "SBP" else None
        bitconce_wallet.number = self.number
        bitconce_wallet.limit = self.limit
        bitconce_wallet.autonumber_off = self.auto_number_off
        bitconce_wallet.notify_off = self.notify_off
        bitconce_wallet.description = self.description

        return bitconce_wallet

    def add_requisite_on_platform(self) -> None:
        bitconce_wallet = self.to_bitconce_wallet()

        if not self.repo.edit_wallet(bitconce_wallet, 'add'):
            raise Exception("Реквизит не добавлен!")

        self.is_active = True

        """реквизит добавляется включенным, поэтому сразу выключаем"""
        self.toggle_enable_on_platform()

    def toggle_enable_on_platform(self) -> None:
        """нужно получить id реквизита в БД платформы"""
        self.initialize()

        self.repo.toggle_enable(wallet_id=self.base_id, enable=not self.is_active)

    def delete_requisite_on_platform(self) -> None:
        bitconce_wallet = self.to_bitconce_wallet()

        if not self.repo.edit_wallet(bitconce_wallet, 'delete'):
            raise Exception("Реквизит не удален!")
