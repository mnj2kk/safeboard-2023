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

@app.post("/api/sleep_process")
async def update_process(body: str = Body(...)):
    global process_thread
    match body:
        case 'start':
            if not process.status():
                process_thread = update_thread()
                process_thread.start()
                return 'Process started.'
            return 'Process is already running.'
        case 'stop':
            if not process.status():
                return 'Procces has already been stopped.'
            process.kill()
            process_thread = update_thread()
            return 'Process stopped.'
        case _:
            return 'Invalid body %s, for POST /api/sleep_process.' % body