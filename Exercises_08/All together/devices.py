# This Python script is written by Vinay Reddy B

class CustomDevice:
    pi = 3.142

    def __init__(self) -> None:
        print("Running constructor for base class")
        self.debug = False

    def run(self):
        raise NotImplementedError("This is an abstract class, do not instantiate")

    def calculate_crc(self, frame: str) -> int: 
        print("Checking CRC from base")
        crc = 123456789
        return crc

class CustomFirewall(CustomDevice):

    def __init__(self, parameter1) -> None:
        CustomDevice.__init__(self)
        print(f"Running constructor for {parameter1}")
        self.parameter1 = parameter1
        self.test_message = ""
    
    def configure_firewall(self):
        print("Configuring Firewall")

    def calculate_crc(self, frame: str) -> int: 
        print("Checking CRC from child")
        crc = 123456789
        return crc

class CustomSwitch(CustomDevice):

    def __init__(self, parameter1) -> None:
        CustomDevice.__init__(self)
        print(f"Running constructor for {parameter1}")
        self.parameter1 = parameter1
        self.test_message = ""
    
    def configure_switch(self):
        print("Configuring Switch")

    def calculate_crc(self, frame: str) -> int: 
        print("Checking CRC from child")
        crc = 123456789
        return crc

class CustomLoadBalancer(CustomDevice):

    def __init__(self, parameter1) -> None:
        CustomDevice.__init__(self)
        print(f"Running constructor for {parameter1}")
        self.parameter1 = parameter1
        self.test_message = ""
    
    def configure_load_balancer(self):
        print("Configuring Load Balancer")

    def calculate_crc(self, frame: str) -> int: 
        print("Checking CRC from child")
        crc = 123456789
        return crc
