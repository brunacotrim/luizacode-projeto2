from fastapi import APIRouter

router_home = APIRouter(
    prefix=""
)

@router_home.get("/")
def home():
    return {"status": "API Ativa"}