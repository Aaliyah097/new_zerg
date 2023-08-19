import sqlalchemy.exc

from src.platforms.model.platform import Platform
from src.platforms.service import PlatformFabric
from db.tables import Platforms, Base, select, update


class PlatformRepo:
    @staticmethod
    def create_platform(platform: Platform) -> None:
        try:
            with Base() as session:
                new_platform = Platforms(
                    token=platform.token,
                    name=platform.name,
                    source=platform.source
                )
                session.add(new_platform)
        except sqlalchemy.exc.IntegrityError:
            pass

    @staticmethod
    def delete_platform(token: str) -> None:
        with Base() as session:
            my_platform = session.get(Platforms, token)
            if my_platform:
                session.delete(my_platform)

    @staticmethod
    def update_platform(platform: Platform) -> None:
        with Base() as session:
            query = update(Platforms).where(Platforms.token == platform.token).\
                values(
                token=platform.token,
                name=platform.name,
                source=platform.source
            )
            session.execute(query)

    @staticmethod
    def get_platform(token: str) -> Platform | None:
        with Base() as session:
            my_platform = session.get(Platforms, token)

            if not my_platform:
                return None

            return PlatformFabric.get_platform(
                token=my_platform.token,
                name=my_platform.name,
                source=my_platform.source
            )

    @staticmethod
    def get_all_platforms() -> list[Platform]:
        with Base() as session:
            query = select(Platforms)
            my_platforms = []

            for p in session.scalars(query).all():
                my_platforms.append(
                    PlatformFabric.get_platform(
                        token=p.token,
                        name=p.name,
                        source=p.source
                    )
                )

            return my_platforms
