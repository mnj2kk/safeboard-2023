from fastapi import FastAPI, Body
from .process_handler import ProcessHandler
from threading import Thread

app = FastAPI()

process = ProcessHandler()

async def update_thread():
    return Thread(target=process.run)

process_thread = update_thread()

@app.get("/api/sleep_process")
async def get_status():
    return 'Procces is running.' if process.status() else 'Process is not running.'
