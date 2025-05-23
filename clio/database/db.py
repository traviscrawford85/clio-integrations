# a script to initialize the database for token storage
# This script creates the necessary tables and initializes the database for storing Clio API tokens.
# It uses SQLAlchemy for ORM and SQLite as the database backend.
# database/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///clio_tokens.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
