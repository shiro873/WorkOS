import structlog
import logging


def configure_logging(level: str):
    logging.basicConfig(level=level)

    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer(),
        ]
    )
