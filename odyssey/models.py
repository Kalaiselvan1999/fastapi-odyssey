from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    is_active: Mapped[bool] = mapped_column(default=True)


class Odyssey(Base):
    __tablename__ = "odyssey"

    name: Mapped[str] = mapped_column(nullable=True)
    departure: Mapped[str]
    destination: Mapped[str]

    def __str__(self) -> str:
        return f"{self.name}"
