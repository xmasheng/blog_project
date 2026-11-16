
from sqlalchemy import Integer, String, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.session import Base


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    space_id: Mapped[int] = mapped_column(
        ForeignKey("spaces.id"),
        nullable=False,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    space: Mapped["Space"] = relationship(
        "Space",
        back_populates="posts"
    )

