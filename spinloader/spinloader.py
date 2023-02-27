from .threads import _AnimationThread 
from . import TextColor,ConsoleSettings
import sys
import json 
import time
import threading 

def animate(message:str="Processing",timeout:float=None,animation:list=None,spinner_color:TextColor=TextColor.yellow,delay:float=0.1):
    """
    Use this decorator to call the function along with a spinloader.

    PARAMS:
        - message -> This is the message desplayed along with the spinloader
        - timeout -> Time (in seconds) to wait before raising the ThreadTimeoutError  
        - animation -> The sequences to use 
        - spinner_color -> The color of the spinner. Takes in the TextColor object 
        - delay -> The delay between each frame 
    
    RETURNS:
        - The return value of the function
    """
    if animation is None:
        # In case no animation is passed, we default over to this one
        animation = ["( ●    )","(  ●   )","(   ●  )","(    ● )","(     ●)","(    ● )","(   ●  )","(  ●   )","( ●    )","(●     )"]

    def _outer(function):
        def _inner(*args,**kwargs):
            try:
                # A custom thread subclass
                _threadObj = _AnimationThread(function,*args,**kwargs) 
                _threadObj.start()
                ConsoleSettings.hide_cursor()
                _running = True
                _distance_from_message = len(message) + 40

                while _running:
                    for _ in animation:
                        ConsoleSettings.clear_line()
                        print(f"{message:<{_distance_from_message}}{spinner_color(_)}",end="\r")
                        ConsoleSettings.clear_line()
                        time.sleep(delay)
                        if _threadObj.check(timeout):
                            _running = False
                            break
                            
            finally:
                # show_cursor inside the finally block so that this method is called atleast once 
                ConsoleSettings.show_cursor()
            return _threadObj.join() # returning the return value of the function
        return _inner 
    return _outer 