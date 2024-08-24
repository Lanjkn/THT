
from fastapi.responses import JSONResponse

ACCOUNTS: dict = {}

def deposit_balance(
    destination: str,
    amount: int
):
    try:
        if destination in ACCOUNTS:
            account = ACCOUNTS[destination]
            account["balance"] += amount
            return JSONResponse({"destination": {"id": destination, "balance": account["balance"]}}, status_code=201)
        
        else:
            account: dict = {
                "id": destination,
                "balance": amount
            }
            ACCOUNTS[destination] = account

            return JSONResponse({"destination": {"id": destination, "balance": amount}}, status_code=201)
    except Exception as e:
        raise e
    
def withdraw_balance(
    origin: str,
    amount: int
):
    try:
        if origin in ACCOUNTS:
            account = ACCOUNTS[origin]
            account["balance"] -= amount

            return JSONResponse({"origin": {"id": origin, "balance": account["balance"]}}, status_code=201)
        
        else:
            return JSONResponse(0, status_code=404)
    
    except Exception as e:
        raise e
    
def transfer_balance(
    origin: str,
    destination: str,
    amount: int
):
    try:
        if destination not in ACCOUNTS:
            ACCOUNTS[destination] = {"id": destination, "balance": 0}
        
        if origin in ACCOUNTS:
            ACCOUNTS[origin]["balance"] -= amount
            ACCOUNTS[destination]["balance"] += amount
            
            return JSONResponse({
                "origin": {"id": origin, "balance": ACCOUNTS[origin]["balance"]},
                "destination": {"id": destination, "balance": ACCOUNTS[destination]["balance"]}
            }, status_code=201)
        
        else:
            return JSONResponse(0, status_code=404)
    
    except Exception as e:
        raise e
    
def get_account_balance(
    account_id: str
):
    try:
        if account_id in ACCOUNTS:
            return ACCOUNTS[account_id]["balance"]
        
        else:
            return JSONResponse(0, status_code=404)
    
    except Exception as e:
        raise e
    
def reset_accounts():
    global ACCOUNTS
    ACCOUNTS = {}

