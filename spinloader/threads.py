from .exceptions import ThreadTimeoutError
import threading 
import time 
import sys

class _AnimationThread(threading.Thread):
    """
    This is a custom sub-class of the Thread class. This has some added benefits 
    1. Captures return values 
    2. Can add timeouts
    """
    def __init__(self,function,*args,**kwargs):
        # initializing the Thread class. 
        super().__init__(daemon=True)
        self.args = args
        self.kwargs = kwargs
        self.function = function
        # variable used to capture the return value 
        self.return_value = None 
        # used in timeouts 
        self.complete = False

    def run(self):
        # starting a clock to keep tract of the start time 
        self.start_time = time.monotonic()
        self.return_value =  self.function(*self.args,**self.kwargs)
        self.complete = True
        
    def join(self):
        return self.return_value

    def check(self,timeout):
        if timeout is not None:
            if (time.monotonic()-self.start_time)>timeout:
                raise ThreadTimeoutError("Thread Operation Timed Out")
        return self.complete
