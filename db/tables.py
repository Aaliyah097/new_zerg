from sqlalchemy import (
    String, Float, Boolean, Integer, select, ForeignKey, create_engine, update
)
from typing import List, Optional
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from . import config

engine = create_engine(
    config.DB_URL,
    echo=True
)


class Base(DeclarativeBase):
    session = None

    def __enter__(self):
        self.session = Session(engine)
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Если в config.py установлено COMMIT = False, то откатывать все транзакции (используется при тестах)"""
        if self.session:
            if exc_type or exc_val:
                self.session.rollback()
                raise Exception("Rollback %s, %s, %s" % (str(exc_type), str(exc_val), str(exc_tb)))
            else:
                if config.COMMIT:
                    self.session.commit()
                else:
                    self.session.rollback()
            self.session.close()
            self.session = None


class Platforms(Base):
    __tablename__ = "platforms"

    name: Mapped[str] = mapped_column(String(30))
    source: Mapped[str] = mapped_column(String(30))
    token: Mapped[str] = mapped_column(String(512), unique=True, primary_key=True)

    def __repr__(self) -> str:
        return f"Platform {self.name}, {self.source}, {self.token}"


class Users(Base):
    __tablename__ = 'users'

    telegram: Mapped[str] = mapped_column(String(50), unique=True, primary_key=True)
    telegram_id: Mapped[str] = mapped_column(String(30), default=None, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean(), default=False)

    def __repr__(self) -> str:
        return f"User {self.telegram}, {self.telegram_id}, {self.is_active}"


class Wallets(Base):
    __tablename__ = "wallets"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, unique=True)

    user_id: Mapped[str] = mapped_column(ForeignKey("users.telegram"))
    user: Mapped["Users"] = relationship()

    currency: Mapped[str] = mapped_column(String(30))
    balance: Mapped[float] = mapped_column(Float(), default=0)

    def __repr__(self) -> str:
        return f"Wallet {self.user_id}, {self.balance} {self.currency}"


class Requisites(Base):
    __tablename__ = "requisites"

    direction: Mapped[str] = mapped_column(String(30))
    number: Mapped[str] = mapped_column(String(30), primary_key=True, unique=True)
    owner: Mapped[str] = mapped_column(String(50))
    account: Mapped[str] = mapped_column(String(50), nullable=True, default=None)
    description: Mapped[str] = mapped_column(String(50), nullable=True, default=None)
    is_active: Mapped[bool] = mapped_column(Boolean(), default=False)
    is_hidden: Mapped[bool] = mapped_column(Boolean(), default=False)

    wallet_id: Mapped[str] = mapped_column(ForeignKey("wallets.id"))
    wallet: Mapped["Wallets"] = relationship()

    user_id: Mapped[str] = mapped_column(ForeignKey("users.telegram"))
    user: Mapped["Users"] = relationship()

    platform_id: Mapped[str] = mapped_column(ForeignKey('platforms.token'))
    platform: Mapped["Platforms"] = relationship()

    def __repr__(self) -> str:
        return f"Requisites {self.platform_id}, {self.user_id}, {self.number}"
