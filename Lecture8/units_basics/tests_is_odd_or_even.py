import is_odd_or_even_module as om

def test_is_odd_or_even_2():
    assert om.is_odd_or_even(2) == True, "error case: 2"
    

def test_is_odd_or_even_3():
    assert om.is_odd_or_even(3) == False, "error case: 3"


def test_is_odd_or_even_21():
    assert om.is_odd_or_even(21) == True, "error case: 21"
    
    
def test_is_odd_or_even_0():
    assert om.is_odd_or_even(0) == True, "error case: 0"
    

def test_is_odd_or_even_4():
    assert om.is_odd_or_even(-4) == True, "error case: -4"