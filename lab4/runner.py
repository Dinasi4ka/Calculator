import sys
import os

lab4_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lab4", "src"))
sys.path.append(lab4_root)

from src.main import main

if __name__ == "__main__":
    main()