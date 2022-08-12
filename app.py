import uvicorn
from fastapi import FastAPI
from fastapi import APIRouter
from starlette.middleware.cors import CORSMiddleware
from scripts.core.services import candidate_services,login
app = FastAPI()
# app.include_router(candidate_services.router1)
app.include_router(candidate_services.router2)
# app.include_router(login.app1)

# app.include_router(post_api.router1)
# app.include_router(put_api.router2)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE", "PUT"],
    allow_headers=["*"]
)

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=5001, log_level="info")

router1=APIRouter()
router2 = APIRouter()
app=APIRouter()

