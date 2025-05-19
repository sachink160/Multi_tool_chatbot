from fastapi import FastAPI, Depends
from app.routes import user_routes, rag_rout, tools_rout
from app.database import Base, engine
from app.auth import get_current_user
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_routes.router)
app.include_router(rag_rout.router)
app.include_router(tools_rout.router)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or replace with your frontend's origin, like "http://localhost:5500"
    allow_credentials=True,
    allow_methods=["*"],  # Or ["GET", "POST", "OPTIONS", "PUT", "DELETE"]
    allow_headers=["*"],  # Or ["Authorization", "Content-Type"]
)

@app.get("/profile", tags=["Profile"])
def get_profile(current_user: str = Depends(get_current_user)):
    return {"message": "Welcome", "user": current_user}
