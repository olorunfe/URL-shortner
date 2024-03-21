from fastapi import FastAPI
from routers import router
from database import connect_to_database, disconnect_from_database

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
async def startup():
    await connect_to_database()

@app.on_event("shutdown")
async def shutdown():
    await disconnect_from_database()
