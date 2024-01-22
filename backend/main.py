import uvicorn
import logging
import sys
from contextlib import asynccontextmanager

from fastapi import FastAPI
from backend.config import settings
from backend.routers.main import api_router
from backend import __version__
from backend.database import sessionmanager

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG if settings.debug else logging.INFO)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Function that handles startup and shutdown events.
    To understand more, read https://fastapi.tiangolo.com/advanced/events/
    """
    yield
    if sessionmanager._engine is not None:
        # Close the DB connection
        await sessionmanager.close()


def get_application() -> FastAPI:
    application = FastAPI(
        lifespan=lifespan,
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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8086)
