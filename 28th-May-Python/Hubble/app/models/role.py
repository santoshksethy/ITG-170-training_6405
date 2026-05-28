from sqlalchemy import Column, Integer, String
from ..db.base import Base

class Role(Base):
    __tablename__ = "roles"

    role_id = Column(Integer, primary_key=True, index=True)
    role = Column(String(1), unique=True, nullable=False)  # h, d, t, m