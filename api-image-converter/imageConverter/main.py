import uvicorn
import os
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from icecream import ic


from config import *
from routers import devops

ic.configureOutput(prefix = 'ic| -> ')

logging.basicConfig(level = logging.DEBUG)
logging.info('Start /v' + api_v + '/' + api)


app = FastAPI(
    name = "API Image Converter",
    title = "/api.image.converter",
    description = "API to convert picture in specific format.",
    version = "1.0.1",
    openapi_url = '/v' + api_v + '/' + api + '/openapi.json',
    docs_url = '/v' + api_v + '/' + api + '/docs',
    redoc_url = None,
    terms_of_service = "https://api.koden.solutions/terms.html",
    contact = {
        "name": "Koden",
        "url": "https://www.koden.solutions",
        "email": "support@koden.solutions",
    },
    openapi_tags = [
        {
            'name': 'metric',
            'description': "paths for metric",
            "externalDocs": {
                "description": "External docs",
                "url": "https://www.pebble.solutions",
            }
        },
        {
            'name': 'variable',
            'description': "paths for variable",
            "externalDocs": {
                "description": "External docs",
                "url": "https://www.pebble.solutions",
            }
        },
        {
            'name': 'devops',
            'description': "paths for devops",
            "externalDocs": {
                "description": "External docs",
                "url": "https://www.pebble.solutions",
            }
        }
    ],
    responses=responses_default
)

# origins = ["http://127.0.0.1:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["GET", "POST", "PUT", "DELETE"],
    allow_headers = ["*"],
)

app.include_router(
    devops.router,
    tags = ["devops"],
    prefix = "/v" + api_v + "/" + api
)

if __name__ == "__main__" and os.environ.get("ENVIRONMENT") != "PRODUCTION":
    uvicorn.run(app, host = "127.0.0.1", port = 3000)
