import json


class JsonData:
    def __init__(self):
        with open("transaction.json") as read_file:
             self.data = json.load(read_file)
             self.tax_rate =self.data["taxes"][0]["rate"]
             self.price_with_tax = self.data["total_collected_money"]["amount"]
             self.net_sale = self.data["itemization"][0]["net_sales_money"]["amount"]
    
    def validate(self):
        net_sale_calculated  = int(self.price_with_tax / (self.tax_rate+1))
        print("The net sale calculated is:", net_sale_calculated)
        print("The net sale from the file:", self.net_sale)
        if (net_sale_calculated) == (self.net_sale):
            return("The net sale calculated is equal to the net sale retrieved from JSON file")
        else:
            return("The net sale calculated is not equal to the net sale retrieved from JSON file")


test1 = JsonData()
print(test1.validate())