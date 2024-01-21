import uvicorn
from fastapi import FastAPI
from backend.config import settings
from backend.routers.main import api_router
from backend import __version__
from backend.db import models, database


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.app_name,
        docs_url="/apidoc",
        redoc_url=None,
        openapi_url=f"{settings.api_prefix}/openapi.json",
        version=__version__.app_version,
        description=__version__.app_description
    )

    application.include_router(api_router)

    return application


# Get app from factory
app = get_application()


# DB init on startup
@app.on_event("startup")
def init_db():
    models.Base.metadata.create_all(bind=database.engine)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8086)
