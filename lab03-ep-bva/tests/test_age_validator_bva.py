from src.age_validator import is_valid
import pytest

@pytest.mark.parametrize("age,expected", [
    (17,False),
    (18,True),
    (66, False)
])
def test_boundaries_parametrize(age, expected):
    assert is_valid(age) == expected