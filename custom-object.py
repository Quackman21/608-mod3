# Python object representing a purchase for a given amount
class Purchase(int):
    def _init_(self, amount):
        self.amount = amount

    def calculateTax(self, taxPercent):
        return self.amount * taxPercent/100.0

    def calculateTip(self, tipPercent):
        return self.amount * tipPercent/100.0

    def calculateTotal(self, taxPercent, tipPercent):
        return self.amount * (1 + taxPercent/100.0 + tipPercent/100.0)

# Create purchase object given an amount
purchase = Purchase(100.0) 

# Set the tax and tip percentages
initial = 100.0
taxPercent = 7.5
tipPercent = 20.0

# Use the object to calculate tax and tip
initialPrice = purchase._init_(initial)
tax = purchase.calculateTax(taxPercent)
tip = purchase.calculateTip(tipPercent)

# Display some useful information
print ('Tax: ',tax)
print ('Tip: ',tip)
print ('Total: ', purchase.calculateTotal(taxPercent, tipPercent))
