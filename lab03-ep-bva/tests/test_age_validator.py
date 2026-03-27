from src.age_validator import is_valid

#Ep
#ep1 age < 18 : 10
# ep2 age = 18-65 : 30
# ep3 age > 65 : 70

def test_ep1_age_10_invalid():
    assert not is_valid(10)

def test_ep2_age_30_valid():
    assert is_valid(30)

def test_ep3_age_70_invalid():
    assert not is_valid(70)