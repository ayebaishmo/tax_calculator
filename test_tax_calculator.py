import pytest
from tax_calculator import calculate_tax

def test_calculate_tax():
    assert calculate_tax(0) == "No tax"
    assert calculate_tax(5000) == 0
    assert calculate_tax(12000) == 0
    assert calculate_tax(20000) == 1600
    assert calculate_tax(36000) == 4800
    assert calculate_tax(40000) == 6400
    assert calculate_tax(50000) == 10400

def test_negative_earnings():
    with pytest.raises(ValueError, match="Earnings cannot be negative"):
        calculate_tax(-5000)