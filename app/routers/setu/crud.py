# -*- coding: utf-8 -*-
from databases import Database

async def get_setu_count(db: Database) -> int:
    data = await db.fetch_one("select count(*) from setu")
    return data[0]
