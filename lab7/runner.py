import sys
import os

lab7_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lab7"))
sys.path.append(lab7_root)

from src.main import main

if __name__ == "__main__":
    main()