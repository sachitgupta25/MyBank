from env_settings import *
import os
from bank_opertions.operations import Operations
from main import show_welcome_screen, initialize, display_menu


if __name__ == "__main__":
    initialize()
    show_welcome_screen()
    # Run only first time. Not afterwards. Use file arguments
    display_menu()
