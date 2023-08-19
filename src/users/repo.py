import sqlalchemy.exc

from src.users.model.user import User
from db.tables import Base, Users, select, update


class UserRepo:
    @staticmethod
    def create_user(user: User) -> None:
        try:
            with Base() as session:
                new_user = Users(
                    telegram=user.telegram,
                    telegram_id=user.telegram_id,
                    is_active=user.is_active
                )
                session.add(new_user)
        except sqlalchemy.exc.IntegrityError:
            pass

    @staticmethod
    def get_all_users() -> list[User]:
        with Base() as session:
            query = select(Users)
            return [
                User(
                    telegram=u.telegram,
                    telegram_id=u.telegram_id,
                    is_active=u.is_active
                ) for u in
                session.scalars(query).all()
            ]

    @staticmethod
    def get_user(telegram: str) -> User | None:
        with Base() as session:
            my_user = session.get(Users, telegram)

            if not my_user:
                return None

            return User(
                telegram=my_user.telegram,
                telegram_id=my_user.telegram_id,
                is_active=my_user.is_active
            )

    @staticmethod
    def delete_user(telegram: str) -> None:
        with Base() as session:
            my_user = session.get(Users, telegram)
            if my_user:
                session.delete(my_user)

    @staticmethod
    def update_user(user: User) -> None:
        with Base() as session:
            query = update(Users).where(Users.telegram == user.telegram).\
                values(
                telegram=user.telegram,
                telegram_id=user.telegram_id,
                is_active=user.is_active
            )
            session.execute(query)
