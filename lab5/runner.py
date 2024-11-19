import sys
import os

lab5_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lab5"))
sys.path.append(lab5_root)

from src.main import main

if __name__ == "__main__":
    main()