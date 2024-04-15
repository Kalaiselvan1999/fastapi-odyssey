from typing import List, Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    is_active: Mapped[bool] = mapped_column(default=True)


class User(Base):
    __tablename__ = "user"

    name: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(unique=True)
    company: Mapped[Optional[str]]

    addresses: Mapped[List["Address"]] = relationship(back_populates="user", cascade="all, delete-orphan")

    def __str__(self) -> str:
        return f"{self.name} - {self.email}"


class Address(Base):
    __tablename__ = "address"

    city: Mapped[str]
    state: Mapped[str]
    country: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    user: Mapped["User"] = relationship(back_populates="addresses")

    def __str__(self) -> str:
        return f"{self.city}"
