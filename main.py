from fastapi import FastAPI
from app.api.router import router
#from app.db.db import engine

#importa e excuta metadade do Base Engine
#Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(router)