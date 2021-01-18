class SaleItem:
    def __init__(self, name, cost, tax, count):
        self.name = name
        self.cost = cost
        self.tax = tax
        self.count = count

        self.total_cost = count * cost * tax
    def get_name(self):
        return self.name
    
    def get_total_cost(self):
        return self.total_cost

my_item = SaleItem("Spoon", 2.00, 1.01, 2)
print(my_item.get_name())
print(my_item.get_total_cost())

shopping = []
shopping.append(my_item)
hand = shopping.pop()
print(hand.get_name())
    
