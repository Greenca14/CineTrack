import uuid
from datetime import datetime
from decimal import Decimal
from sqlalchemy import JSON, DateTime, Integer, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base

class Film(Base):
    __tablename__ = "films"


    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    kinopoisk_id: Mapped[id] = mapped_column(
        Integer, unique=True, nullable=False, index=True
    )
    title: Mapped[str] = mapped_column(String(500), nullable=False)
    original_title: Mapped[str | None] = mapped_column(String(500), nullable=True)
    year: Mapped[int | None] = mapped_column(Integer, nullable=True)
    poster_path: Mapped[str | None] = mapped_column(String(500), nullable=True)
    genres: Mapped[list] = mapped_column(JSON, default=list, nullable=True)
    runtime: Mapped[int | None] = mapped_column(Integer, nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    rating_kp: Mapped[Decimal | None] = mapped_column(Numeric(3, 1), nullable=True)
    rating_imdb: Mapped[Decimal | None] = mapped_column(Numeric(3, 1), nullable=True)
    cached_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False, index=True
    )