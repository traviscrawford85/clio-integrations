# init_db.py
from clio.database.db import engine
from clio.database.models import Base

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
print("✅ Database reset and initialized.")

