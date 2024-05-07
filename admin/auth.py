from sqladmin import Admin
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse
from fastapi import status, Depends
from apis.v1.router_login import authenticate_user, get_current_user
from core.security import create_access_token
from sqlalchemy.orm import Session

from db.sessions import get_db


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request, db: Session = Depends(get_db)):
        form = await request.form()
        email, password = form["username"], form["password"]

        user = await authenticate_user(email, password, db)
        if user:

            access_token = create_access_token(data={"sub": user.email})
            request.session.update({"token": access_token})

        return True

    async def logout(self, request: Request) -> bool:
        # Usually you'd want to just clear the session
        request.session.clear()
        return True

    async def authenticate(self, request: Request, db: Session = Depends(get_db)):
        token = request.session.get("token")

        if not token:
            return RedirectResponse(request.url_for("admin:login"), status_code=status.HTTP_302_FOUND)

        # Check the token in depth
        user = await get_current_user(token, db)
        if not user:
            return RedirectResponse(request.url_for("admin:login"), status_code=status.HTTP_302_FOUND)

        return True


authentication_backend = AdminAuth(secret_key="...")

