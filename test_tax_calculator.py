import pytest
from tax_calculator import calculate_tax

def test_calculate_tax():
    assert calculate_tax(0) == "No tax"

def test_negative_earnings():
    with pytest.raises(ValueError, match="Earnings cannot be negative"):
        calculate_tax(-5000)