# clio/calculators.py
# Business logic like statute of limitations computation
from datetime import datetime, timedelta


def compute_limitations_date(incident_date_str: str) -> str:
    """
    Given a date string (ISO format), return a limitations date 2 years in the future.
    Returns in 'YYYY-MM-DD' format.
    """
    try:
        incident_date = datetime.strptime(incident_date_str, "%Y-%m-%d")
        limitations_date = incident_date + timedelta(days=365 * 2)
        return limitations_date.strftime("%Y-%m-%d")
    except ValueError:
        return ""
