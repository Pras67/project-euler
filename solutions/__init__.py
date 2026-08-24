"""
Solutions package containing individual Project Euler problem solutions.
"""

from pathlib import Path

# Extend package search path so subfolders (q1-q50, q51-q100) are directly importable
__path__ = [
    str(p)
    for p in Path(__file__).parent.iterdir()
    if p.is_dir() and not p.name.startswith("__")
] + __path__
