"""
Цей модуль запускає лабораторну роботу 2 з проекту. Він додає шлях до папки lab2
в sys.path і викликає основну функцію з lab2/src/main.py.
"""

import sys
import os
from src.main import main

lab2_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..",  "lab2"))
sys.path.append(lab2_root)

print(f"Шлях до lab2: {lab2_root}")

if __name__ == "__main__":
    main()
