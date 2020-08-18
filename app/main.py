import sys

from app.application import app
from app.routes import article_router

sys.path.extend(["./"])

ROUTERS = (article_router,)

for router in ROUTERS:
    app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8888, log_level="info")
