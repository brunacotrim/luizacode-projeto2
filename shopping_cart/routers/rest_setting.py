from fastapi import FastAPI

from shopping_cart.routers.home import router_home
from shopping_cart.routers.users import router_users
from shopping_cart.routers.products import router_products


def routes_setting(app: FastAPI):
    app.include_router(router_home)
    app.include_router(router_users)
    app.include_router(router_products)

def make_app_fastapi():
    app = FastAPI()
    routes_setting(app)

    return app
