# token_store.py
from datetime import datetime, timedelta
from database.db import SessionLocal
from database.models import ClioToken

def store_tokens(access_token: str, refresh_token: str, expires_in: int):
    session = SessionLocal()
    try:
        expires_at = datetime.utcnow() + timedelta(seconds=expires_in)
        token = ClioToken(
            access_token=access_token,
            refresh_token=refresh_token,
            expires_at=expires_at
        )
        session.merge(token)
        session.commit()
    finally:
        session.close()

def get_access_token() -> str:
    session = SessionLocal()
    try:
        token = session.query(ClioToken).first()
        if not token or token.expires_at < datetime.utcnow():
            raise Exception("Access token missing or expired.")
        return token.access_token
    finally:
        session.close()
