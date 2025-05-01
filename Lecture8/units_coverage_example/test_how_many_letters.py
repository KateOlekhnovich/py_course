import how_many_letters as hml

def test_no_letters():
    assert hml.howmanyletters("") == 'no data'

def test_less_than_3_letters():
    assert hml.howmanyletters("NO") == "less than three letters!?"
    
def test_more_than_3_letters():
    assert hml.howmanyletters("lol :)") ==['lol', ':)']