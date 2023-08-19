from src.users.model.user import User
from src.wallets.model.wallet import Wallet
from db.tables import Base, Wallets, select, Users


class WalletRepo:
    @staticmethod
    def get_wallet_by_user(user: User, currency: str) -> Wallet | None:
        query = select(Wallets).where(Wallets.user_id == user.telegram)
        with Base() as session:
            wallet = session.scalars(query).first()
            if not wallet:
                return None

            my_wallet = Wallet(
                    user=user,
                    currency=currency,
                )
            my_wallet.id = wallet.id
            my_wallet.balance = wallet.balance
            return my_wallet

    @staticmethod
    def create_wallet(user: User, wallet: Wallet) -> None:
        with Base() as session:
            new_wallet = Wallets(
                user_id=user.telegram,
                currency=wallet.currency,
                balance=wallet.balance
            )
            session.add(new_wallet)

    @staticmethod
    def get_all_wallets() -> list[Wallet]:
        query = select(Wallets)
        my_wallets = []

        with Base() as session:
            for w in session.scalars(query).all():
                my_wallet = Wallet(
                    currency=w.currency,
                    user=User(
                        telegram=w.user.telegram,
                        telegram_id=w.user.telegram_id,
                        is_active=w.user.is_active
                    )
                )
                my_wallet.id = w.id
                my_wallet.balance = w.balance
                my_wallets.append(my_wallet)

        return my_wallets

    @staticmethod
    def delete(wallet: Wallet) -> None:
        query = select(Wallets).where(Wallets.user_id == wallet.user.telegram,
                                      Wallets.currency == wallet.currency)

        with Base() as session:
            wallet = session.scalars(query).first()
            if wallet:
                session.delete(wallet)
