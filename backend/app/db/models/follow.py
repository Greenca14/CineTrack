from datetime import datetime
from sqlalchemy import CheckConstraint, DateTime, ForeignKey, PrimaryKeyConstraint, String, func
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base

class Follow(Base):
    __tablename__ = "follows"
    __table_args__ = (
        PrimaryKeyConstraint("follower_id", "followee_id", name="pk_follows"),
        CheckConstraint("follower_id != followee_id", name="pk_follows"),
    )

    follower_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("users.id", ondelete="CASCADE",), nullable=False
    )
    followee_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("users.id", ondelete="CASCADE",), nullable=False, index=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )