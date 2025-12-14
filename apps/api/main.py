from fastapi import FastAPI
from packages.common.config import settings
from packages.common.logging import configure_logging
from apps.api.routes.health import router as health_router


configure_logging(settings.log_level)

app = FastAPI(title=settings.app_name)

app.include_router(health_router)
