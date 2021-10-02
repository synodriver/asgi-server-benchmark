# -*- coding: utf-8 -*-
from pathlib import Path

from databases import Database


sqlite = None


async def on_start():
    global sqlite
    sqlite_path: str = str(Path(__file__).parent / "setu.db")
    sqlite = Database(f"sqlite:///{sqlite_path}")
    await sqlite.connect()


async def on_shutdown():
    global client
    client.close()
    await sqlite.disconnect()
