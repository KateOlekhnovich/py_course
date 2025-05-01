class MobilePhone:
    def __init__(self, number):
        self.number = number
        self.switch = False
    def turn_on(self):
        self.switch = True
        return f"Mobile phone {self.number} is enabled"
    def turn_off(self):
        self.switch = False
        return f"Mobile phone {self.number} is turned off"
    def call(self, cally):
        if self.switch:
            return f"Mobile phone is calling {cally}"
        else:
            return f"Turn on the Mobile Phone"
    def __repr__(self):
        return f"Mobile phone is {self.number} status: {self.switch}"
