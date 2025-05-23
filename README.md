```clio_integration/
├── clio/
│   ├── matters.py        # Wrapper for Clio's matters API using matter_show, matter_index, etc.
│   ├── contacts.py       # Wrapper for Clio's contacts API (contact_index, contact_show)
│   ├── tasks.py          # Wrapper for Clio's tasks API (task_index, task_show, task_create)
│   ├── calendar.py       # Wrapper for Clio's calendar and events API (event_index, calendar_index)
│   ├── activities.py     # Wrapper for Clio's activities API (activity_index, activity_create)
│   ├── notes.py          # Wrapper for Clio's notes API (note_index, note_create)
│   ├── validators.py     # Validates phone numbers, custom fields like Date of Incident
│   └── calculators.py    # Business logic like statute of limitations computation
├── database/
│   ├── db.py             # SQLAlchemy setup and session maker
│   └── models.py         # ClioToken model for token storage
├── token_store.py        # Functions to store and retrieve access tokens securely
├── oauth.py              # Handles initial token exchange and optional refresh
├── oauth_endpoints.py    # FastAPI endpoint to capture OAuth redirect
├── openapi_client/       # Generated Clio client SDK (locally vendored)
│   ├── __init__.py
│   └── ... (generated modules)
├── webhooks.py           # FastAPI routes for handling Clio webhook events
├── main.py               # FastAPI app entry point
├── Dockerfile            # Container image for the Clio integration
├── requirements.txt      # Project dependencies
└── .env.example          # Example environment configuration
```