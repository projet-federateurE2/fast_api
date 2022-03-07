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

charset = {"Content-Type": "application/json; charset=utf-8"}

""" 
@app.middleware("http")
async def add_charset(request: Request, call_next):
    response = await call_next(request)
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response 
"""


if(os.environ.get("ENV") != "dev"):
    @app.middleware("http")
    async def verify_JTW_token(request: Request, call_next):
        try:
            oto = request.headers["otoroshi-claim"]
        except:
            return JSONResponse(status_code=400, content={"erreur": "Pas de token Otoroshi", "info": "L'URL utilisée ne passe pas par le reverse-proxy"})

        try:
            token = jwt.decode(oto, os.environ.get("JWT_SECRET"), audience = os.environ.get("JWT_AUDIENCE"), algorithms = "HS256")
            request.token = token
            response = await call_next(request)
            return response
        except jwt.exceptions.InvalidTokenError as error:
            logging.error(error)
            return JSONResponse(status_code=401, content={"erreur": "Mauvais token JWT", "token": oto })
        except BaseException as error:
            logging.error(error)
            return JSONResponse(status_code=500, content={"erreur": "Erreur du token JWT", "info": error })


# List all routes
@app.get("/")
def list_all_routes():
    url_list = [{"path": route.path, "name": route.name}
                for route in app.routes]
    return JSONResponse(url_list, headers= charset)

app.include_router(router_proprietaire, tags=["Proprietaire"], prefix="/v1")
app.include_router(router_artisan, tags=["Artisan"], prefix="/v1")
app.include_router(router_projet, tags=["Projet"], prefix="/v1")

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
    openapi_schema["security"] = [{
        "basicAuth": []
    }]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = auth_openapi
