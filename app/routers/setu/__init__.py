# -*- coding: utf-8 -*-
from fastapi import APIRouter
from fastapi.responses import UJSONResponse

import app.db as db

from .crud import get_setu_count
router=APIRouter(prefix="/api/v1")


@router.get("/setu/count", summary="query number", response_class=UJSONResponse)
async def count():
    count = await get_setu_count(db.sqlite)
    return {"count": count}
