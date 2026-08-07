"""
Unit tests for Question 15: Lattice Paths.
"""

from solutions.q015_lattice_paths import (
    solve,
    solve_combinatorics,
    solve_lattice_paths,
)


def test_q015_sample():
    # 2x2 grid has 6 routes
    assert solve(2) == 6
    assert solve_combinatorics(2) == 6
    assert solve_lattice_paths(2) == 6


def test_q015_full():
    # 20x20 grid has 137846528820 routes
    assert solve(20) == 137846528820
    assert solve_combinatorics(20) == 137846528820
    assert solve_lattice_paths(20) == 137846528820
