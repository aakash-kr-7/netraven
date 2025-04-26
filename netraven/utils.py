from colorama import Fore, Style, init

init(autoreset=True)

def color_print(msg, color="white"):
    color_map = {
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "cyan": Fore.CYAN,
        "white": Fore.WHITE
    }
    print(color_map.get(color, Fore.WHITE) + msg + Style.RESET_ALL)
