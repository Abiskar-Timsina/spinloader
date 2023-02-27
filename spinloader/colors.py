class TextColor: 
    """
    This class contains the static definations for all the different colors. None of these write to the screen but instead return the string back to be uses as required.
    """
    @staticmethod
    def black(message:str)->str:
        return (f'\033[0;30m{message}\033[0m') 

    @staticmethod
    def red(message):
        return (f'\033[0;31m{message}\033[0m') 
    
    @staticmethod
    def green(message):
        return (f'\033[0;32m{message}\033[0m') 

    @staticmethod
    def yellow(message):
        return (f'\033[0;33m{message}\033[0m') 

    @staticmethod
    def blue(message):
        return (f'\033[0;34m{message}\033[0m') 

    @staticmethod
    def megenta(message):
        return (f'\033[0;35m{message}\033[0m') 

    @staticmethod
    def cyan(message):
        return (f'\033[0;36m{message}\033[0m') 

    @staticmethod
    def white(message):
        return (f'\033[0;37m{message}\033[0m') 

class ConsoleSettings:
    """
    This class is useful to perform basic line clearing and console operation that are used in the spinloader.
    """
    @staticmethod
    def clear_line():
        print("\033[K",end="")
    
    @staticmethod
    def hide_cursor():
        print("\033[?25l",end="")
    
    @staticmethod
    def show_cursor():
        print("\033[?25h",end="")