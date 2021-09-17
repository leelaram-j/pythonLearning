# Single Inheritance

class nokia:
    company = "Nokia India"
    website = "www.nokia.com"

    def contact_details(self):
        print("Address: abc road, Chennai")

class nokia1100(nokia):
    def __init__(self):
        self._name = "Nokia 1100"
        self._year = 1998

    def printProductDetails(self):
        print("Name: ", self._name)
        print("Year: ", self._year)
        print("Company: ", self.company)
        print("Website: ", self.website)

mobile = nokia1100()
mobile.printProductDetails()
mobile.contact_details()