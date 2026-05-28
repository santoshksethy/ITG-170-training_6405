from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Status(Base):
    __tablename__ = "statuses"

    status_id = Column(Integer, primary_key=True, index=True)
    status = Column(String(1), unique=True, nullable=False)  # a, i, p, b