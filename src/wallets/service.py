from src.users.model.user import User
from src.users.repo import UserRepo
from src.wallets.model.wallet import Wallet
from src.wallets.repo import WalletRepo


class WalletService:
    def __init__(self):
        self.user_repo = UserRepo
        self.wallet_repo = WalletRepo

    def create_new_wallet(self, user: User, currency: str) -> None:
        wallet = Wallet(
            user=user,
            currency=currency
        )

        if self.wallet_repo.get_wallet_by_user(user, currency):
            return
        else:
            self.wallet_repo.create_wallet(user=user, wallet=wallet)
