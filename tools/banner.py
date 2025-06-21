from colorama import init, Fore, Style

init(autoreset=True)

def print_banner():
    banner = f"""
{Fore.CYAN}{Style.BRIGHT}    
  ______   _______ ___   ___  _     ____   _____  __
 |  _ \ \ / /_   _/ _ \ / _ \| |   | __ ) / _ \ \/ /
 | |_) \ V /  | || | | | | | | |   |  _ \| | | \  / 
 |  __/ | |   | || |_| | |_| | |___| |_) | |_| /  \ 
 |_|    |_|   |_| \___/ \___/|_____|____/ \___/_/\_\
                                                    
                                                    
{Fore.YELLOW}               PyToolbox — Kullanışlı Python Araçları Seti
{Fore.MAGENTA}                 https://github.com/KarapinarAhmet/Pytoolbox
"""
    print(banner)
