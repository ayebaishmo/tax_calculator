import pytest
from tax_calculator import calculate_tax

def test_calculate_tax():
    assert calculate_tax(0) == "No tax"