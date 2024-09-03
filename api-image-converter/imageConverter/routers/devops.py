from typing import List

from fastapi import APIRouter, status, Query, Body
from icecream import ic
from imageConverter.config import *
from metric.schemas.healthcheckResponseSchemas import HealthcheckResponseSchema

router = APIRouter(
    responses=responses_default
)


@router.get("/healthchecker/",
            name="Simple healthcheck",
            summary="Simple healthcheck",
            description="Simple healthcheck",
            response_description="Confirmation message",
            responses=responses_healthcheck,
            status_code=status.HTTP_200_OK)
async def healthcheck():
    """ Healthcheck
    """
    message = f'API /v{api_v}/{api} is LIVE!'
    return {"message": message}
