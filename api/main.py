from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="FastAPI on Vercel - All Methods Example")

@app.get("/")
def get_user():
    return JSONResponse({"message": "This is sample elysium fastapi"})

@app.get("/user")
def get_user():
    return JSONResponse({"message": "User Returned"})

@app.post("/user")
def create_user():
    return JSONResponse({"message": "User Created"})

@app.put("/user")
def update_user():
    return JSONResponse({"message": "User Updated"})

@app.delete("/user")
def delete_user():
    return JSONResponse({"message": "User Deleted"})