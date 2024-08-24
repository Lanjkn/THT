
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from service.event_and_balance_service import deposit_balance, get_account_balance, withdraw_balance, transfer_balance


event_and_balance_router = APIRouter()

@event_and_balance_router.post("/event")
def account_event(
    json_sent: dict,
):
    if "type" not in json_sent:
        return JSONResponse({"error": "No type of event"}, status_code=400)
    
    if json_sent["type"] == "deposit":
        return deposit_balance(json_sent["destination"], json_sent["amount"])
    elif json_sent["type"] == "withdraw":
        return withdraw_balance(json_sent["origin"], json_sent["amount"])
    elif json_sent["type"] == "transfer":
        return transfer_balance(json_sent["origin"], json_sent["destination"], json_sent["amount"])

    else:
        return JSONResponse({"error": "Invalid type of event"}, status_code=400)
    
@event_and_balance_router.get("/balance")
def account_balance(
    account_id: str
):
    return get_account_balance(account_id)