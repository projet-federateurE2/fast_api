import logging
import os
import jwt
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.openapi.utils import get_openapi

from app.routes.route_proprietaire import router_proprietaire
from app.routes.route_artisan import router_artisan
from app.routes.route_projet import router_projet

app = FastAPI()


if(os.environ.get("ENV") != "dev"):
    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next):
        try:
            oto = request.headers["otoroshi-claim"]
        except:
            return JSONResponse(status_code=400, content={"erreur": "Pas de token Otoroshi"})

        try:
            token = jwt.decode(oto, os.environ.get("JWT_SECRET"), audience="api-dev", algorithms = "HS256")
            request.token = token
            response = await call_next(request)
            return response
        except BaseException as e:
            logging.error("os.environ" + os.environ.get("JWT_SECRET"))
            logging.error(e)
            return JSONResponse(status_code=401, content={"erreur": "Mauvais token JWT", "token": oto })


# List all routes
@app.get("/")
def list_all_routes():
    url_list = [{"path": route.path, "name": route.name}
                for route in app.routes]
    return url_list


app.include_router(router_proprietaire, tags=["v1"], prefix="/v1")

app.include_router(router_artisan, tags=["v1"], prefix="/v1")

app.include_router(router_projet, tags=["v1"], prefix="/v1")


def auth_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="FastAPI",
        version="2.0.0",
        description="Projet APIrénov",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"]= {
        "basicAuth": {
            "type": "http",
            "scheme": "basic"
        }
    }
    openapi_schema["security"] = {
        "basicauth": []
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = auth_openapi
