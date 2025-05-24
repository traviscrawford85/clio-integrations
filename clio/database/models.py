# clio/database/models.py
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ClioToken(Base):
    __tablename__ = "clio_tokens"

    access_token = Column(String, primary_key=True)
    refresh_token = Column(String)
    token_type = Column(String)  # ✅ This must match your DB schema
    expires_at = Column(DateTime)

