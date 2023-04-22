from subprocess import Popen

class ProcessHandler(object):
    def __init__(self):
        self.runnable = False
        self.last_status = -1

    def run(self):
        self.runnable = True
        self.process = Popen(['python3', 'app/sleep_process.py'])
        while not (self.process is None) and self.process.poll() is None:
            pass
        if not (self.process is None):
            self.last_status = self.process.poll()
        self.runnable = False
    
    def kill(self):
        self.process.kill()
        self.runnable = False
        self.last_status = 2
        self.process = None
    
    def status(self):
        return self.runnable