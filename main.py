from fastapi import FastAPI
from app.api.router import router
#from app.db.db import engine
from fastapi_pagination import add_pagination

#importa e excuta metadade do Base Engine
#Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(router)

add_pagination(app)