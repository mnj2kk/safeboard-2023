from fastapi import FastAPI, Body
from fastapi.responses import PlainTextResponse
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
get_status.__doc__ = "GET /api/sleep_process request (curl -X GET 0.0.0.0:80/api/sleep_process) to check the status of the process."

@app.get("/api/sleep_process/result")
async def get_result():
    if process.last_status == -1:
        return '404 Not Found'
    return process.last_status
get_result.__doc__ = "GET /api/sleep_process/result (curl -X GET 0.0.0.0:80/api/sleep_process/result) to check last return code of the proces."

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
update_process.__doc__ = "POST {body} /api/sleep_process (curl -X POST -d \"body\" 0.0.0.0:80/api/sleep_process) to update process status (stop or start)."

@app.get("/api/docs", response_class=PlainTextResponse)
async def docs():
    return "{}\n{}\n{}".format(get_status.__doc__, get_result.__doc__, update_process.__doc__)