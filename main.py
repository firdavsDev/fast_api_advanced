import uvicorn
from celery import Celery
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# IMPORT ROUTERS
from ecommerce.cart import router as cart_router
from ecommerce.orders import router as order_router
from ecommerce.products.routers import category as category_router
from ecommerce.products.routers import product as product_router
from ecommerce.user import router as user_router
from ecommerce.auth import router as auth_router
from ecommerce import config

app = FastAPI(
    title="FastAPI Advanced Tutorial",
    description="This is a very fancy project, with auto docs for the API and everything. More: https://www.jetbrains.com/pycharm/guide/tutorials/fastapi-aws-kubernetes",
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS
origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:8080",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include all routers
app.include_router(user_router.router)
app.include_router(category_router.router)
app.include_router(product_router.router)
app.include_router(cart_router.router)
app.include_router(order_router.router)
app.include_router(auth_router.router)

celery = Celery(
    __name__,
    broker=f"redis://{config.REDIS_HOST}:{config.REDIS_PORT}/{config.REDIS_DB}",
    backend=f"redis://{config.REDIS_HOST}:{config.REDIS_PORT}/{config.REDIS_DB}",

)

celery.conf.imports = [
    "ecommerce.orders.tasks",
]

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        log_level="info",
        reload=True,
        timeout_keep_alive=60 * 60 * 24 * 7,
        workers=4,
    )
