import enum
import uuid
from sqlalchemy import String, DateTime, Enum
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

Base = declarative_base()

class Status(enum.Enum):
    CREATED = 'created',
    DELETED = 'deleted'

class Deployments(Base):
    __tablename__ = 'deployments'
    id: Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4(), primary_key=True)
    db_name: Mapped[str] = mapped_column(String(30))
    status: Mapped[Enum] = mapped_column(Enum(Status))
    username: Mapped[str] = mapped_column(String(30))
    creation_time: Mapped[DateTime] = mapped_column(DateTime)
