from sqlalchemy import Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.session import Base


class Space(Base):
    __tablename__ = "spaces"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True,
        nullable=False
    )

    title: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        default="我的個人空間"
    )

    theme: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="default"
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="space"
    )

