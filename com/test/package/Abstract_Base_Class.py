from abc import ABC, abstractmethod

class Bank(ABC):
    # here Bank is Abstract class as it inherited ABC

    @abstractmethod
    def loan(self):
        pass

    @abstractmethod
    def credit(self):
        pass

    @abstractmethod
    def debit(self):
        pass

class HDFCBank(Bank):
    def loan(self):
        print("loan at 10%")

    def credit(self):
        print("Credit at 48%")

    def debit(self):
        print("Debit card")

o = HDFCBank()
o.loan()
o.credit()
o.debit()

## Please note that we need to define the function definition in the inherited class.