# backend/main.py
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()

# Read env variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*")  # allow set e.g. https://your-frontend-url

if not SUPABASE_URL or not SUPABASE_SERVICE_ROLE_KEY:
    raise RuntimeError("SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY must be set as environment variables")

# create supabase admin client (server only)
supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)

app = FastAPI(title="FastAPI + Supabase Admin Example")

# Set up CORS for front-end origin(s)
origins = [o.strip() for o in ALLOWED_ORIGINS.split(",")] if ALLOWED_ORIGINS != "*" else ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmptyRequest(BaseModel):
    # placeholder; you can extend if you want to accept params (pagination etc.)
    pass

@app.post("/users")
async def list_users(body: EmptyRequest | None = None):
    """
    POST /users
    Returns a page (up to 1000) of auth users from Supabase Admin API.
    This uses the server-side admin SDK - NEVER expose the service role key in the browser.
    """
    try:
        # Using supabase-py admin endpoint
        resp = supabase.auth.admin.list_users(page=1, per_page=1000)
        # Response format contains e.g. resp.data, resp.error, but supabase-py returns a dict-like
        users = None
        # supabase-py returns python object with 'data' or 'users' depending on version; normalize safely
        if isinstance(resp, dict):
            users = resp.get("users") or resp.get("data") or resp
        else:
            # try attribute access
            users = getattr(resp, "data", None) or getattr(resp, "users", None) or resp

        return {"users": users}
    except Exception as e:
        # Do not leak secrets; log in real server
        raise HTTPException(status_code=500, detail=f"Failed to list users: {str(e)}")
 
