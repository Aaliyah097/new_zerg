from src.users.repo import UserRepo
from src.wallets.repo import WalletRepo
from src.platforms.repo import PlatformRepo
from src.requisites.model.bitconce_requisite import BitconceRequisite


TEST_TELEGRAM = "@thedawnofmydeath"
TEST_TOKEN = "aa244a53-c35d-4545-a3c4-35df391bdfa2"


def cycle_on_platform():
    """create, toggle, delete"""
    user = UserRepo.get_user(TEST_TELEGRAM)
    platform = PlatformRepo.get_platform(TEST_TOKEN)
    wallet = WalletRepo.get_wallet_by_user(user, "USDT")

    req = BitconceRequisite(
        direction="CARD",
        number="1111 2222 3333 4444",
        owner="Павел Олегович О.",
        account="",
        platform_token=platform.token,
        user_telegram=user.telegram,
        wallet_currency=wallet.currency
    )

    req.add_requisite_on_platform()
    req.delete_requisite_on_platform()


def test_():
    cycle_on_platform()
    pass
