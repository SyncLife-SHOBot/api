import uuid
from typing import Dict, Optional, Any
from datetime import datetime, timedelta
from fastapi import HTTPException, Header


class InMemorySessionService:
    _sessions: Dict[str, Dict[str, Any]] = {}
    _session_duration = timedelta(hours=1)

    @classmethod
    def create_session(cls, user_id: str) -> str:
        session_token = str(uuid.uuid4())
        cls._sessions[session_token] = {
            "user_id": user_id,
            "created_at": datetime.now(),
        }
        return session_token

    @classmethod
    def get_user_from_session(cls, session_token: str) -> Optional[str]:
        session = cls._sessions.get(session_token)
        if (
            session
            and isinstance(session.get("created_at"), datetime)
            and datetime.now() - session["created_at"] < cls._session_duration
        ):
            return str(session["user_id"])
        cls.delete_session(session_token)
        return None

    @classmethod
    def delete_session(cls, session_token: str) -> None:
        if session_token in cls._sessions:
            del cls._sessions[session_token]

    @classmethod
    async def validate_session_token(cls, session_token: str = Header(...)) -> str:
        user_id = cls.get_user_from_session(session_token)
        if not user_id:
            raise HTTPException(status_code=401, detail="Sesión inválida o expirada")
        return user_id
