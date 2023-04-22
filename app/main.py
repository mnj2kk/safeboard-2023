from fastapi import FastAPI, Body
from .process_handler import ProcessHandler
from threading import Thread

app = FastAPI()

process = ProcessHandler()

def update_thread():
    return Thread(target=process.run)

process_thread = update_thread()

@app.get("/api/sleep_process")
async def get_status():
    return 'Procces is running.' if process.status() else 'Process is not running.'

@app.get("/api/sleep_process/result")
async def get_result():
    if process.last_status == -1:
        return '404 Not Found'
    return process.last_status