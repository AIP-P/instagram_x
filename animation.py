import time
import os
import sys
import pyfiglet

def clear_console():
    # Clears the console
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_animation(duration):
    end_time = time.time() + duration
    loading_text = pyfiglet.figlet_format("LOADING")
    while time.time() < end_time:
        for dots in range(1, 4):
            clear_console()
            sys.stdout.write(loading_text + '.' * dots + ' ' * (3 - dots))
            sys.stdout.flush()
            time.sleep(0.5)
        sys.stdout.write('\r' + ' ' * (len(loading_text.split('\n')[0]) + 3))  # clear the dots for the next loop
        sys.stdout.flush()
        time.sleep(0.5)
def titile() : 
    loading_animation(10)  # Run the loading animation for 10 seconds
    clear_console()
    print(pyfiglet.figlet_format("Brahma kamala"))
