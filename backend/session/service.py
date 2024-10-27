from fastapi import APIRouter, HTTPException, Response, Request
from itsdangerous import URLSafeTimedSerializer


router = APIRouter()

class SessionService:

    secret_key = "edumeet-secret-key"

    def __init__(self):
        self.serializer = URLSafeTimedSerializer(self.secret_key)


    @router.get("/create-session")
    async def create_session(self, request: Request):

        session_id = self.serializer.dumps(request.client.host)
        response = Response("success")
        response.set_cookie(key="session_id", value=session_id)
        return response
    

    @router.get("/profile")
    async def verify_session(self, request: Request):
        session_id = request.cookies.get("session_id")

        try:
            self.serializer.loads(session_id, max_age=3600)  
            return {"status": "success",
                    "session_id": session_id}
        except:
            raise HTTPException(status_code=401, detail="Invalid session")
        
