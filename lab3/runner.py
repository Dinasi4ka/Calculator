"""
Цей модуль запускає лабораторну роботу 3 з проекту. Він додає шлях до папки lab3
в sys.path і викликає основну функцію з lab3/src/main.py.
"""

import sys
import os
from src.main import main

lab3_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lab3"))
sys.path.append(lab3_root)

print(f"Шлях до lab3: {lab3_root}")


if __name__ == "__main__":
    main()
