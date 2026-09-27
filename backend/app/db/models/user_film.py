import uuid
from datetime import datetime, date
from sqlalchemy import Boolean, CheckConstraint, DateTime, ForeignKey, String, Text, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from enum import StrEnum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.db.models.film import Film

class FilmStatus(StrEnum):
    NOT_WATCHED = "not_watched"
    PLANNED = "planned"
    WATCHING = "watching"
    WATCHED = "watched"
    ON_HOLD = "on_hold"
    DROPPED = "dropped"

class UserFilm(Base):
    __tablename__ = "user_films"
    __table_args__ = (
        UniqueConstraint("user_id", "film_id", name="uq_user_film"),
        CheckConstraint(
            "status IN ('not_watched', 'planned', 'watching', 'watched', 'on_hold', 'dropped')",
            name="ck_user_film_status",
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
    status: Mapped[str] = mapped_column(
        String(20), nullable=False, default=FilmStatus.NOT_WATCHED.value, index=True
    )
    is_favorite: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )
    
    film: Mapped["Film"] = relationship("Film", lazy="joined")
