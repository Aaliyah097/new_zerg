from src.wallets.service import WalletService
from src.wallets.model.wallet import Wallet
from src.users.repo import UserRepo
from src.wallets.repo import WalletRepo
from src.users.model.user import User

TEST_TELEGRAM = "@thedawnofmydeath"


def create():
    currency = 'USDT'
    user = UserRepo.get_user(TEST_TELEGRAM)
    service = WalletService()

    for i in range(2):
        service.create_new_wallet(
            user=user, currency=currency
        )

    # нельзя создать на одного пользователя два кошелька в одной валюте
    wallet_by_user = WalletRepo.get_wallet_by_user(user, currency)
    assert isinstance(wallet_by_user, Wallet)

    # допустимые валюты USDT и BTC
    try:
        Wallet(user, 'RUB')
    except:
        pass
    else:
        assert False


def get_all():
    wallets = WalletRepo.get_all_wallets()
    if len(wallets) > 0:
        assert isinstance(wallets[0], Wallet) and isinstance(wallets[0].user, User)


def delete():
    currency = "USDT"
    user = UserRepo.get_user(TEST_TELEGRAM)
    wallet_by_user = WalletRepo.get_wallet_by_user(user, currency)
    if wallet_by_user:
        WalletRepo.delete(wallet_by_user)


def test_():
    create()
    get_all()
    #delete()
    pass
