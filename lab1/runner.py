import sys
import os

from src.main import main

lab1_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(lab1_root)

if __name__ == "__main__":
    main()