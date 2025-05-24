import sys
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Add the parent directory to sys.path so clio_integrations can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clio.database.models import ClioToken  # Make sure this import path is correct

# Example: replace with your actual database URL
engine = create_engine('sqlite://///home/sysadmin01/clio-integrations/clio_tokens.db')
Session = sessionmaker(bind=engine)
session = Session()

token = session.query(ClioToken).first()
if token is not None:
	print("Type of token.access_token:", type(token.access_token))
else:
	print("No token found.")
