import sys
import os

lab8_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(lab8_root)

from src.main import main

if __name__ == "__main__":
    main()