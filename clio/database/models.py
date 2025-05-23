# database/models.py
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()

class ClioToken(Base):
    __tablename__ = "clio_tokens"

    access_token = Column(String, primary_key=True)
    refresh_token = Column(String)
    expires_at = Column(DateTime)
