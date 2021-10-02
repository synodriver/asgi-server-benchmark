# -*- coding: utf-8 -*-
import time

from fastapi import FastAPI,Request

from .routers import setu
from .db import on_shutdown, on_start

app = FastAPI()

app.include_router(setu.router)

app.on_event("startup")(on_start)
app.on_event("shutdown")(on_shutdown)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
