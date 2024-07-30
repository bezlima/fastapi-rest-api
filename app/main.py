from fastapi import FastAPI
from .routes.user_routes import user_router
from .routes.login_routes import login_router
from .db.db import engine
from .models import user_model

user_model.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_router)
app.include_router(login_router)
