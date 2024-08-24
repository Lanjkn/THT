from fastapi import FastAPI
from router.event_and_balance import event_and_balance_router
from router.reset import reset_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(event_and_balance_router)
app.include_router(reset_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

