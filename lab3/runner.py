import sys
import os

lab3_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(lab3_root)

from src.main import main

if __name__ == "__main__":
    main()