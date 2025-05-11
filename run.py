import sys
import os

sys.path.append(os.path.abspath("../HexRoot"))

from click.bot import Bot

if __name__ == "__main__":
    Bot().start()
