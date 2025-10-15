Env vars required:
- SUPABASE_URL=https://<project>.supabase.co
- SUPABASE_SERVICE_ROLE_KEY=sb_... (service role or secret key; server only)
- ALLOWED_ORIGINS=https://your-frontend-url.com  (or * for dev)

Run locally:
$ pip install -r requirements.txt
$ export SUPABASE_URL=...
$ export SUPABASE_SERVICE_ROLE_KEY=...
$ uvicorn main:app --reload --port 8000

POST to /users (body can be empty). Response: {"users": [...]}
 
