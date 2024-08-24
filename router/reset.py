
from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse

from service.event_and_balance_service import reset_accounts

reset_router = APIRouter()

@reset_router.post("/reset", status_code=200)
def reset():
    reset_accounts()
    return Response(bytes("OK", "utf-8"),status_code=200)