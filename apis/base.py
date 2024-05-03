from fastapi import APIRouter

from apis.v1 import router_user, router_blog


api_router = APIRouter()
api_router.include_router(router_user.router, prefix="", tags=["users"])
api_router.include_router(router_blog.router, prefix="/blog", tags=["blogs"])