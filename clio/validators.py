# clio/validators.py
# Validates phone numbers, custom fields like Date of Incident
import re
from typing import Any


def validate_phone_number(phone: str) -> bool:
    # E.164 format: +[country code][number], e.g., +15555555555
    return bool(re.fullmatch(r"\\+\\d{10,15}", phone))


def validate_date_of_incident(custom_fields: dict[str, Any]) -> bool:
    return "Date of Incident" in custom_fields and bool(custom_fields["Date of Incident"])


def validate_matter_data(matter: dict[str, Any]) -> list[str]:
    errors = []

    # Validate phone number
    if "client" in matter and "phone" in matter["client"]:
        phone = matter["client"]["phone"]
        if not validate_phone_number(phone):
            errors.append("Client phone number is not in E.164 format.")
    else:
        errors.append("Client phone number is missing.")

    # Validate Date of Incident custom field
    custom_fields = matter.get("custom_fields", {})
    if not validate_date_of_incident(custom_fields):
        errors.append("Date of Incident is missing or improperly formatted.")

    return errors
