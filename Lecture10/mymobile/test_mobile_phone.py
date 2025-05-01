import mobile_phone_class as mob

def test_constructor():
    phone = mob.MobilePhone("7776224")
    assert phone.number == "7776224"
    assert phone.switch == False

def test_turn_on():
    phone = mob.MobilePhone("7776224")
    result = phone.turn_on()
    assert result == "Mobile phone 7776224 is enabled"
    assert phone.switch == True
    
def test_turn_off():
    phone = mob.MobilePhone("7776224")
    result = phone.turn_off()
    assert result == "Mobile phone 7776224 is turned off"
    assert phone.switch == False
    
def test_call_turned_on():
    phone = mob.MobilePhone("7776224")
    phone.turn_on()
    result = phone.call("Подними трубку")
    assert result == "Mobile phone is calling Подними трубку"
    
def test_call_turned_off():
    phone = mob.MobilePhone("7776224")
    result = phone.call("Подними трубку")
    assert result == "Turn on the Mobile Phone"
    
    
def test_repr():
    phone = mob.MobilePhone("7776224")
    result = repr(phone)
    assert result == "Mobile phone is 7776224 status: False"