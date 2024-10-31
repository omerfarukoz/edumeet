from fastapi import FastAPI
from backend.session.service import router as session_router


app = FastAPI()

app.include_router(prefix="/edumeet/session", router=session_router)