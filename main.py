from fastapi import FastAPI
from routers.users import router as users_router
from services.db_service import Base, engine
app = FastAPI()
app.include_router(users_router)
Base.metadata.create_all(bind=engine)
@app.get("/")
async def root():
    return {"message": "API IS WORKING!"}

