from q3 import attendance

def test_eligible():
    assert attendance(100, 80) == "Eligible"