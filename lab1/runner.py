"""
Цей модуль запускає лабораторну роботу 1 з проекту. Він додає шлях до папки lab1
в sys.path і викликає основну функцію з lab1/src/main.py.
"""

import sys
import os
from src.main import main

lab1_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..",  "lab1"))
sys.path.append(lab1_root)

if __name__ == "__main__":
    main()
    