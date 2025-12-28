from sqlalchemy import (
    Column,
    Index,
    Text,
    String,
    TIMESTAMP,
    text,
)
from sqlalchemy.dialects.postgresql import JSONB

from .base import Base


class IngestState(Base):
    __tablename__ = "ingest_state"
    __table_args__ = (
        Index("idx_ingest_state_name_target", "name", "target"),
        {"schema": "ingest"},
    )

    name = Column(Text, primary_key=True, nullable=False)
    target = Column(
        String(50),
        primary_key=True,
        nullable=False,
        server_default=text("'all'"),
    )
    last_run = Column(TIMESTAMP(timezone=True))
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))


class IngestCheckpoints(Base):
    __tablename__ = "ingest_checkpoints"
    __table_args__ = (
        Index("idx_ingest_checkpoints_name_target", "name", "target"),
        {"schema": "ingest"},
    )

    name = Column(Text, primary_key=True, nullable=False)
    target = Column(
        String(50),
        primary_key=True,
        nullable=False,
        server_default=text("'all'"),
    )
    data = Column(JSONB, nullable=False, server_default=text("'{}'::jsonb"))
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))