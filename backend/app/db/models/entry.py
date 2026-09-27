import uuid
from datetime import datetime, date
from sqlalchemy import Boolean, CheckConstraint, Date, DateTime, ForeignKey, SmallInteger, String, Text, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.db.models.film import Film

class Entry(Base):
    __tablename__ = "entries"
    __table_args__ = (
        UniqueConstraint(
            "user_id", "film_id", "watched_at", name="uq_entry_user_film_date"
        ),
        CheckConstraint(
            "rating IS NULL OR (rating BETWEEN 1 AND 10)", name="ck_entry_rating"
        ),
    )

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    user_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    film_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("films.id", ondelete="CASCADE"), nullable=False, index=True
    )
    rating: Mapped[int | None] = mapped_column(SmallInteger, nullable=True)
    review: Mapped[str | None] = mapped_column(Text, nullable=True)
    watched_at: Mapped[date] = mapped_column(Date, nullable=False)
    is_rewatch: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )

    film: Mapped["Film"] = relationship("Film", lazy="joined")
